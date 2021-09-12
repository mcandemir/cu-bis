import os.path
import json
import selenium
import selenium.webdriver


class Agent:
    def __init__(self):
        # read cfg
        self.BASE_DIR = os.path.dirname(__file__) + "/../.."

        with open(self.BASE_DIR + "/config.json", "r") as f:
            self.cfg = json.load(f)

        # TESTING <---------------------->
        self.set_webdriver()
        self.set_url(self.cfg["urls"]["login"])
        self.login()
        self.set_url(self.cfg["urls"]["obs"])
        self.close()
        # TESTING <---------------------->

    def set_webdriver(self):    # todo: add chrome
        print("<*> setting up driver..")
        options = selenium.webdriver.FirefoxOptions()
        options.set_headless(True)
        self.driver = selenium.webdriver.Firefox(executable_path=self.BASE_DIR + "/cubis/webdrivers/geckodriver",
                                                 options=options)
        print("<*> driver is set!")

    def set_url(self, url):
        print("<*> connecting {}".format(url))
        self.driver.get(url)
        print("<*> connection set!")

    def login(self):
        print("<*> logging in..")
        username_box = self.driver.find_element_by_id(self.cfg["login_page"]["input_username_id"])
        password_box = self.driver.find_element_by_id(self.cfg["login_page"]["input_password_id"])
        login_button = self.driver.find_element_by_id(self.cfg["login_page"]["button_login_id"])
        username_box.send_keys(self.cfg["login_data"]["username"])
        password_box.send_keys(self.cfg["login_data"]["password"])
        login_button.click()
        print("<*> logged in!")

    def close(self):
        print("<*> closing client..")
        self.driver.close()


def main():
    agent = Agent()
