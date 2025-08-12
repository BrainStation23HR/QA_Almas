import os
import pytest
import configparser
from loguru import logger
from utils.common_func import get_latest_log_file, extract_logs
from playwright.sync_api import Playwright, expect, Page

expect.set_options(timeout=60_000)

@pytest.fixture(scope='function')
def config():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _file = os.path.join(cur_dir, "config.ini")
    parser = configparser.ConfigParser()
    parser.read(_file)
    return parser


@pytest.fixture(scope='function')
def data():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _file = os.path.join(cur_dir, "data.ini")
    parser = configparser.ConfigParser()
    parser.read(_file)
    return parser


@pytest.fixture(scope="session", autouse=True)
def setup_logger(request):
    log_format = "{time} | {level} | {message} | {file} | {line} | {" \
                 "function} | {exception}"

    path = "logs/log_{time}.log"

    logger.add(
        sink=path,
        colorize=True,
        format=log_format,
        level='DEBUG',
        compression='zip',
        rotation='50 MB',
        encoding='utf-8',
        retention='30 days',
        backtrace=False,
        diagnose=False,
        catch=True
    )
    yield


screenshots_dir = "reports/screenshots"
screenshots = "screenshots"
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    latest_log = None
    log_data = None
    outcome = yield
    report = outcome.get_result()

    pytest_html = item.config.pluginmanager.getplugin("html")

    if report.when == "call":
        page = item.funcargs.get("page")
        if report.failed:
            logger.error(f"Test failed: {item.nodeid}")
            latest_log = get_latest_log_file("logs")

        if page:
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            logger.info(f"Taking screenshot for {item.name} at {screenshot_path}")
            try:
                page.screenshot(path=screenshot_path)
            except Exception as e:
                print(e)
            if latest_log:
                with open(latest_log) as f:
                    log_data = extract_logs(item.name, latest_log)

            relative_screenshot_path = os.path.join(screenshots, f"{item.name}.png")

            if isinstance(log_data, (str, bytes)):
                report.extra = getattr(report, 'extras', [])
                report.extra.append(pytest_html.extras.html(f"<div><h2>Logs:</h2><pre>{log_data}</pre></div>"))
                report.extra.append(pytest_html.extras.image(relative_screenshot_path))
            else:
                report.extra = getattr(report, 'extras', [])
                report.extra.append(pytest_html.extras.html(f"<div><h2>Logs:</h2><pre>{str(log_data)}</pre></div>"))
                report.extra.append(pytest_html.extras.image(relative_screenshot_path))


@pytest.fixture(scope='session')
def new_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False, args=["--start-fullscreen"])
    # browser = playwright.chromium.launch(headless=True)
    # context = browser.new_context(no_viewport=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()