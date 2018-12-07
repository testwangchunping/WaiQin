# coding=utf-8
from frame.go_homepage import go_Homepage
from frame.delete_blank import delete_blank
from service.change_navigate import *
from config.read_config import ReadConfigFile
from service.change_table import change_table
from service.wq_import import WqImport
from frame.DB_Connect import db_connect


class ReadOldImport(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    readConfig = ReadConfigFile()

    # 未重构的导入
    def read_old_import(self):
        global module_end
        # 查询第一级导航栏
        first_navigate_sql = "SELECT L.id, L.l_module FROM S INNER JOIN T ON T.belong_id = S.id INNER JOIN L ON S.belong_id = L.id AND S.is_old_module = 1 AND L.have_import = 1 GROUP BY L.id"
        # 数据库连接
        first_navigate_data = db_connect(first_navigate_sql)
        for item in first_navigate_data:
            module1_id = str(item[0])
            module1_name = str(item[1])
            # 一级导航栏点击
            module1_name = change_first_navigate(module1_name, self.driver)
            # 查询第二级导航栏
            second_navigate_sql = "SELECT S.id,S.s_module FROM S INNER JOIN L ON S.belong_id = L.id AND S.is_old_module = 1 AND S.have_import = 1 AND S.belong_id = '" + module1_id + "'"
            # 数据库连接
            second_navigate_data = db_connect(second_navigate_sql)
            for item in second_navigate_data:
                module2_id = str(item[0])
                module2_name = str(item[1])
                # 二级导航栏点击
                module2_name = change_second_navigate(module1_name, module2_name, self.driver)
                # 查询tab栏
                tab_sql = "SELECT T.tab FROM T INNER JOIN S ON T.have_import = 1 AND T.belong_id = '" + module2_id + "' GROUP BY T.id"
                tab_data = db_connect(tab_sql)
                tab_list = ''
                for item in tab_data:
                    tab_list = tab_list + str(item[0]) + ' '
                tab_list = delete_blank(str(tab_list).split(' '))
                # 切换tab栏，点击导入按钮
                if len(tab_list):
                    for i in range(len(tab_list)):
                        # 切换tab栏
                        tab_name = change_table(tab_list[i], self.driver)
                        # 导入
                        WqImport(self.driver,self.logger,tab_name).test_old_import()
                else:
                    # 导入
                    WqImport(self.driver, self.logger, module2_name).test_old_import()
                iframe_skip.iframe_exit(self.driver)
            # 页面刷新到首页
            go_Homepage(self.driver, self.logger)

