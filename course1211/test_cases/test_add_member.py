# @Author   : Clifford
# @File     : test_add_member
# @Time     : 2021/12/11 14:38
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_member():
    # 1.登录
    # 2.进入首页页面
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(10)


    # 3.点击"添加成员"按钮
    driver.find_element(By.LINK_TEXT, '添加成员').click()
    time.sleep(3)

    # 4.填写成员信息
    # 4.1 姓名
    # 4.2 acctid
    # 4.3 手机
    driver.find_element(By.NAME, 'username').send_keys('点点')
    driver.find_element(By.NAME, 'acctid').send_keys('1231241241241242124')
    driver.find_element(By.NAME, 'mobile').send_keys('18033335555')
    time.sleep(10)

    # 5.点击"保存"按钮
    # 6.进入通讯录页面
    driver.find_element(By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_btn_save').click()
    time.sleep(3)

    # 7.验证 == > 断言