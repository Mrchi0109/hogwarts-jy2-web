import logging
import time

from selenium.webdriver.common.by import By
from homework.page_objects.base_page import BasePage


class ContactPage(BasePage):
    """
    通讯录页面
    """
    _BTN_ADD_MEMBER = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
    _NAMES_LOC = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

    def click_add_member_button(self):
        """
        点击"添加成员"按钮
        :return:
        """
        logging.info("点击【添加成员】按钮")
        self.do_refresh()
        time.sleep(1)
        self.do_click(*self._BTN_ADD_MEMBER)

        logging.info("==》跳转到添加成员页面")
        from homework.page_objects.member_page import MemberPage
        return MemberPage(self.driver)

    def get_member_names(self):
        """
        获取成员名字列表
        """
        time.sleep(2)
        logging.info("获取成员名字列表")

        elements = self.finds(*self._NAMES_LOC)
        name_list = [ele.get_attribute("title") for ele in elements]

        return name_list