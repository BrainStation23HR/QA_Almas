import configparser
import os


class Locators:

    def locator(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        _file_path = os.path.abspath(cur_dir)[:-8]
        _file = os.path.join(_file_path, "locators.ini")
        parser = configparser.ConfigParser()
        parser.read(_file)
        return parser
