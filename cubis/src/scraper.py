import os.path
import json
import selenium
import selenium.webdriver

class Scraper:
    def __init__(self):
        self.read_config()
        self.set_webdriver()

    def read_config(self):
        # read cfg
        self.BASE_DIR = os.path.dirname(__file__) + "/../.."

        with open(self.BASE_DIR + "/config.json", "r") as f:
            self.cfg = json.load(f)

    def set_webdriver(self):
        options = selenium.webdriver.FirefoxOptions()
        options.set_headless(True)
        self.driver = selenium.webdriver.Firefox(executable_path=self.BASE_DIR + "/cubis/webdrivers/geckodriver",
                                                 options=options)

    def scrape_mainpage(self):
        for element in self.cfg["elements"]["main_page"]:
            print(self.driver.find_element_by_id(self.cfg["elements"]["main_page"][element]).text)

    def scrape_grades(self):
        pass

