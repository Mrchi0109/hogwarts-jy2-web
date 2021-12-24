

def pytest_collection_modifyitems(items):
    """
    处理中文的unicode显示问题
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")