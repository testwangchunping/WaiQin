# coding=utf-8
import unittest
import sys
from frame.screenshoot import get_window_img
from service.read_new_export import ReadNewExport
from frame.logger import Logger
from service.read_old_export import ReadOldExport
from frame.browser_engine import BrowserEngine
from service.login import TestLogin


class TestExport(unittest.TestCase):
    """
    导出用例
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserEngine().get_browser()
        cls.logger = Logger(logger='Export').getlog()
        TestLogin(cls.driver, cls.logger).test_login()

    num = 0

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_old_export(self):
        """
        旧的模块导出
        """
        self.logger.info('开始导出--------------old_export')
        ReadOldExport(self.driver, self.logger).test_old_export()
        self.logger.info('结束导出--------------old_export')
        # 截图
        name = sys._getframe().f_code.co_name
        TestExport.num = self.num + 1
        get_window_img(self, self.logger, name, str(TestExport.num))  # 最后一项为图片第几张

    def test_new_export(self):
        """
        重构模块的导出
        """
        self.logger.info('开始导出--------------new_export')
        ReadNewExport(self.driver, self.logger).test_new_export()
        self.logger.info('结束导出--------------new_export')
        # 截图
        name = sys._getframe().f_code.co_name
        TestExport.num = self.num + 1
        get_window_img(self, self.logger, name, str(TestExport.num))  # 最后一项为图片第几张

    if __name__ == '__main__':
        unittest.main
