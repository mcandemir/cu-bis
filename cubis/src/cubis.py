import os.path
import json
import selenium
import selenium.webdriver


def main():
    # read cfg
    with open(os.path.dirname(__file__) + "/../../config.json", "r") as f:
        cfg = json.load(f)

    # setup driver
    print("setting up driver..")
    driver = selenium.webdriver.Firefox(executable_path=os.path.dirname(__file__) + "/../webdrivers/geckodriver")

    # go to login page and login
    driver.get(cfg["urls"]["login"])

    username_box = driver.find_element_by_id(cfg["login_page"]["input_username_id"])
    password_box = driver.find_element_by_id(cfg["login_page"]["input_password_id"])
    login_button = driver.find_element_by_id(cfg["login_page"]["button_login_id"])

    username_box.send_keys(cfg["login_data"]["username"])
    password_box.send_keys(cfg["login_data"]["password"])

    login_button.click()

    pass

