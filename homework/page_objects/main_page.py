import logging
import time

from selenium.webdriver.common.by import By

from homework.page_objects.base_page import BasePage


class MainPage(BasePage):
    """
    首页
    """

    _BTN_ADD_MEMBER = (By.LINK_TEXT, '添加成员')
    _MENU_CONTACT = (By.ID, 'menu_contacts')

    def go_to_contact_member(self):
        """
        去往通讯录页面
        """

        logging.info("点击【通讯录】菜单")
        self.do_click(*self._MENU_CONTACT)

        logging.info("==》跳转到通讯录页面")
        from homework.page_objects.contact_page import ContactPage
        return ContactPage(self.driver)

    def click_add_member_button(self):
        """
        点击"添加成员"按钮
        :return:
        """

        logging.info("点击【添加成员】按钮")
        self.do_click(*self._BTN_ADD_MEMBER)

        logging.info("==》跳转到添加成员页面")
        from homework.page_objects.member_page import MemberPage
        return MemberPage(self.driver)