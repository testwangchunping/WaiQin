# coding=utf-8

from frame.go_homepage import go_Homepage
from frame.delete_blank import delete_blank
from frame.open_excel import open_excel
from frame.iframe_skip import iframe_skip
from service.change_navigate import change_navigate
from config.read_config import ReadConfigFile
from service.change_table import change_table
from service.wq_import import WqImport


class ReadNewImport(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    readConfig = ReadConfigFile()

    # 新导入，无table项
    def read_new_import(self):
        file_path = self.readConfig.port_data_filepath
        sheet_name = self.readConfig.new_import_sheet
        # 打开excel文件的具体sheet
        try:
            DataSheet = open_excel(file_path, sheet_name)
        except:
            self.logger.debug('导入导出配置文件不存在！')
        # sheet行数
        rowNum = DataSheet.nrows
        for i in range(rowNum):
            module = DataSheet.row_values(i)
            # 去掉字符串中的空格
            module_list = delete_blank(module)
            # 导航栏点击
            module_name = change_navigate(module_list, self.driver)
            # 导入
            WqImport(self.driver, self.logger, module_name).test_new_import()
            # 页面刷新到首页
            go_Homepage(self.driver)

    # 新导出，有table项
    def read_new_import1(self):
        file_path = self.readConfig.port_data_filepath
        sheet_name = self.readConfig.new_import_sheet1
        # 打开excel文件的具体sheet
        DataSheet = open_excel(file_path, sheet_name)
        # sheet行数
        rowNum = DataSheet.nrows
        for i in range(rowNum):
            module = DataSheet.row_values(i)
            module_start = module[0:2]
            module_end = module[2:]
            # 去掉字符串中的空格
            module_start = delete_blank(module_start)  # 导航栏
            module_end = delete_blank(module_end)  # table栏
            # 导航栏点击
            module_name = change_navigate(module_start, self.driver)
            num = len(module_end)
            for j in range(num):
                # 切换table
                module_name = change_table(module_end, j, self.driver)
                # 导入
                WqImport(self.driver, self.logger, module_name).test_new_import()
                iframe_skip.iframe_exit(self.driver)
            # 页面刷新到首页
            go_Homepage(self.driver)
