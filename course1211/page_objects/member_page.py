# @Author   : Clifford
# @File     : member_page
# @Time     : 2021/12/11 15:41
import time

from selenium.webdriver.common.by import By

from course1211.page_objects.base_page import BasePage


class MemberPage(BasePage):

    _INPUT_USERNAME = (By.NAME, 'username')
    _INPUT_ACCTID = (By.NAME, 'acctid')
    _INPUT_MOBILE = (By.NAME, 'mobile')
    _BTN_SAVE = (By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_btn_save')

    def fill_out_member_info(self, name, acctid, mobile):
        """
        填写成员信息
        :return:
        """
        from course1211.page_objects.contact_page import ContactPage
        print("添加成员信息")
        print("点击保存按钮")

        # 4.填写成员信息
        # 4.1 姓名
        # 4.2 acctid
        # 4.3 手机
        self.do_send_keys(*self._INPUT_USERNAME, name)
        self.do_send_keys(*self._INPUT_ACCTID, acctid)
        self.do_send_keys(*self._INPUT_MOBILE, mobile)
        self.do_click(*self._BTN_SAVE)

        return ContactPage(self.driver)

    def fill_out_member_fail(self):
        """
        填写失败
        :return:
        """
        pass