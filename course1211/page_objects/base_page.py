# @Author   : Clifford
# @File     : base_page
# @Time     : 2021/12/11 17:03
import yaml
from selenium import webdriver


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
        else:
            self.driver = driver

    def do_click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def do_send_keys(self, by, locator, value):
        self.driver.find_element(by, locator).send_keys(value)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
