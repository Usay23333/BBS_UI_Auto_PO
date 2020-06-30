# coding=utf-8

import unittest, os
from selenium import webdriver
from page.baidu_pages import BaiduSearch
from time import sleep, strftime
from utils import HTMLTestRunner
from utils.ConfigUtil import ConfigReader
from utils.LoggingUtil import Logger

class Test_BD(unittest.TestCase):

    def test_baidu_search(self):
        driver = webdriver.Chrome()
        bds = BaiduSearch(driver,
                          'https://baidu.com')

        bds.input_value('page object')
        bds.click_search()
        sleep(5)


if __name__ == "__main__":
    # unittest.main()

    log = Logger().instance()

    suite = unittest.TestSuite()
    suite.addTest(Test_BD('test_baidu_search'))

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # 拼接测试报告文件夹：读取项目路径 + report
    report_dir = os.path.join(ConfigReader().get_project("path"), 'reports')
    # 检查测试报告文件夹是否存在，不存在则创建
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)
    # 拼接.html测试报告的路径和文件名，文件名使用格式化时间防止重复，方便根据时间段查询。
    report_path = os.path.join(report_dir, f"{strftime('%Y-%m-%d %H-%M-%S')}.html")
    # 打开一个文件句柄并传给HTMLTestRunner
    f = None
    try:
        f = open(report_path, mode='wb')
        HTMLTestRunner.HTMLTestRunner(
            stream=f,
            verbosity=2,
            title="BBS_UI_Auto",
            description=f"zero_自动化测试报告_{strftime('%Y-%m-%d %H-%M-%S')}"
        ).run(suite)
    except Exception as e:
        log.error(e)
    finally:
        if f: f.close()
