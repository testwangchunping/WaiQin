# coding=utf-8
import os
from frame.go_homepage import go_Homepage
from frame.delete_blank import delete_blank
from frame.open_excel import open_excel
from service.change_navigate import change_navigate
from config.read_config import ReadConfigFile
from service.export import Export
from service.change_table import change_table


class ReadNewExport(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    readConfig = ReadConfigFile()

    # 新导出，无table项
    def test_new_export(self):
        file_path = os.path.abspath(self.readConfig.port_data_filepath)
        sheet_name = self.readConfig.new_export_sheet

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
            # 偶数行（通过link_text获取的模块链接）数据处理
            module_name = change_navigate(module_list, self.driver)
            # 导出照片、导出
            Export(self.driver, self.logger).new_Export(module_name)
            # 页面刷新到首页
            go_Homepage(self.driver)

    # 新导出，有table项
    def test_new_export1(self):
        file_path = os.path.abspath(self.readConfig.port_data_filepath)
        sheet_name = self.readConfig.new_export_sheet1
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
                # 导出照片、导出
                Export(self.driver, self.logger).new_Export(module_name)
            # 页面刷新到首页
            go_Homepage(self.driver)
