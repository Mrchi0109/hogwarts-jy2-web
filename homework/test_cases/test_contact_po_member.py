import pytest
from faker import Faker

from homework.page_objects.main_page import MainPage


def prepare_case_data():
    """
    生成测试数据的函数，用于数据驱动
    """

    # 实例化
    fake = Faker('zh_CN')

    # 批量随机生成测试数据
    case_data = []
    for i in range(3):
        case_data.append([fake.name(), fake.ssn(), fake.phone_number()])

    return case_data

class TestContactMember:
    """
    测试用例：在通讯录页面添加成员
    """

    # 前置条件
    def setup_class(self):
        # 所有测试用例共享一个首页对象
        self.main_page = MainPage()

    # 后置条件
    def teardown_class(self):
        # 关闭浏览器
        self.main_page.driver.quit()

    # 参数化用例
    @pytest.mark.parametrize("name,acctid,mobile", prepare_case_data())
    def test_contact_po_member(self, name, acctid, mobile):

        # 业务逻辑（链式调用）
        name_list = self.main_page\
            .go_to_contact_member()\
            .click_add_member_button()\
            .fill_out_member_info(name=name, acctid=acctid, mobile=mobile) \
            .get_member_names()

        # 断言
        assert name in name_list
