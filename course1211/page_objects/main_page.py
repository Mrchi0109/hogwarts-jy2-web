# @Author   : Clifford
# @File     : main_page
# @Time     : 2021/12/11 15:41
import time

from selenium.webdriver.common.by import By

from course1211.page_objects.base_page import BasePage


class MainPage(BasePage):
    """
    首页
    """

    _BTN_ADD_MEMBER = (By.LINK_TEXT, '添加成员')

    def click_add_member_button(self):
        """
        点击"添加成员"按钮
        :return:
        """
        from course1211.page_objects.member_page import MemberPage

        print("点击添加成员按钮")
        self.do_click(*self._BTN_ADD_MEMBER)
        time.sleep(3)

        return MemberPage(self.driver)