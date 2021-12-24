# @Author   : Clifford
# @File     : test_cookie
# @Time     : 2021/12/10 18:26
import time

import yaml
from selenium import webdriver


class TestCookie:

    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_save_cookies(self):
        # 1. 访问企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 2. 等待20s，人工扫码操作
        time.sleep(10)

        # 3. 等成功登录后， 再去获取cookie信息
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print(cookie)

        # 4. 将 cookie 存入一个本地文件
        with open("cookie.yaml", 'w') as f:
            yaml.safe_dump(cookies, f)

        self.driver.quit()


    def test_add_cookie(self):

        # 1. 访问企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 2. 植入cookie
        cookies = yaml.safe_load(open("cookie.yaml", 'r'))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # 3. 访问主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self.driver.quit()