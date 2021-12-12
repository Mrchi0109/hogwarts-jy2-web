# @Author   : Clifford
# @File     : test_po_member
# @Time     : 2021/12/11 15:51
import time

import yaml
from faker import Faker
from selenium import webdriver

from course1211.page_objects.main_page import MainPage


def test_po_member():
    # 随机造数
    fake = Faker('zh_CN')
    name, acctid, mobile = fake.name(), fake.ssn(), fake.phone_number()

    # 链式调用
    name_list = MainPage()\
        .click_add_member_button()\
        .fill_out_member_info(name=name, acctid=acctid, mobile=mobile)\
        .get_member_names()

    assert name in name_list



