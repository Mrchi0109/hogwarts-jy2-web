import logging
import time

from selenium.webdriver.common.by import By
from homework.page_objects.base_page import BasePage


class MemberPage(BasePage):
    """
    添加成员页面
    """

    _INPUT_USERNAME = (By.NAME, 'username')
    _INPUT_ACCTID = (By.NAME, 'acctid')
    _INPUT_MOBILE = (By.NAME, 'mobile')
    _BTN_SAVE = (By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_btn_save')

    def fill_out_member_info(self, name, acctid, mobile):
        """
        填写成员信息
        :return:
        """
        logging.info("添加成员信息")

        logging.info("输入姓名")
        self.do_send_keys(*self._INPUT_USERNAME, name)

        logging.info("输入acctid")
        self.do_send_keys(*self._INPUT_ACCTID, acctid)

        logging.info("输入手机号")
        self.do_send_keys(*self._INPUT_MOBILE, mobile)

        logging.info("点击保存按钮")
        self.do_click(*self._BTN_SAVE)

        logging.info("==》跳转到通讯录页面")
        from homework.page_objects.contact_page import ContactPage
        return ContactPage(self.driver)
