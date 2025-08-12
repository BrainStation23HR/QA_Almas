import glob
import os

def get_latest_log_file(log_directory, extension="*.log"):
    log_files = glob.glob(os.path.join(log_directory, extension))

    if not log_files:
        return None

    latest_file = max(log_files, key=os.path.getmtime)

    return latest_file


def extract_logs(test_name, log_file):
    with open(log_file, "r") as file:
        logs = file.readlines()

    start_marker = f"{test_name}"
    end_marker = f"{test_name}"

    extracting = False
    test_logs = []

    for line in logs:
        if start_marker in line:
            extracting = True
        if extracting:
            test_logs.append(line)
        if end_marker == start_marker:
            break

    return ''.join(test_logs)

