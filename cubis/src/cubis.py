from .scraper import Scraper


class Agent(Scraper):
    def __init__(self):
        super(Agent, self).__init__()

        # TESTING <---------------------->
        self.set_url(self.cfg["urls"]["login"])
        self.login()
        self.set_url(self.cfg["urls"]["obs"])
        self.show_mainpage()
        self.close()
        # TESTING <---------------------->

    def set_url(self, url):
        print("<*> connecting {}".format(url))
        self.driver.get(url)
        print("<*> connection set!")

    def login(self):
        print("<*> logging in..")
        username_box = self.driver.find_element_by_id(self.cfg["elements"]["login_page"]["input_username_id"])
        password_box = self.driver.find_element_by_id(self.cfg["elements"]["login_page"]["input_password_id"])
        login_button = self.driver.find_element_by_id(self.cfg["elements"]["login_page"]["button_login_id"])
        username_box.send_keys(self.cfg["login_data"]["username"])
        password_box.send_keys(self.cfg["login_data"]["password"])
        login_button.click()
        print("<*> logged in!")

    def show_mainpage(self):
        print()
        self.scrape_mainpage()
        print()

    def close(self):
        print("<*> closing client..")
        self.driver.close()


def main():
    agent = Agent()
