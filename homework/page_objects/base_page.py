import logging

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver=None):

        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

            cookies = yaml.safe_load(open("../data/cookie.yaml", 'r'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            logging.info("==》进入首页")
        else:
            self.driver: WebDriver = driver

    def do_click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def do_send_keys(self, by, locator, value):
        self.driver.find_element(by, locator).send_keys(value)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def do_refresh(self):
        self.driver.refresh()
