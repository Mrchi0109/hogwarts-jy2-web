# @Author   : Clifford
# @File     : contact_page
# @Time     : 2021/12/11 15:42
from selenium.webdriver.common.by import By
from course1211.page_objects.base_page import BasePage

class ContactPage(BasePage):

    _NAMES_LOC = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

    def get_member_names(self):

        print("获取成员名字列表")
        elements = self.finds(*self._NAMES_LOC)
        name_list = [ele.get_attribute("title") for ele in elements]

        return name_list