# coding=utf-8
from frame.DB_Connect import db_connect
from frame.go_homepage import go_Homepage
from service.change_navigate import change_first_navigate
from service.change_navigate import change_second_navigate
from service.export import Export
from service.change_table import change_table
from frame.delete_blank import delete_blank


class ReadNewExport(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    # 重构模块的导出
    def test_new_export(self):
        global module_end
        # 查询第一级导航栏
        first_navigate_sql = "SELECT L.id, L.l_module FROM L WHERE L.is_old_module = 0 AND L.have_export = 1 ORDER BY L.id"
        # 数据库连接
        data1 = db_connect(first_navigate_sql)
        for item in data1:
            module1_id = str(item[0])
            module1_name = str(item[1])
            # 一级导航栏点击
            module1_name = change_first_navigate(module1_name, self.driver)
            # 查询第二级导航栏
            second_navigate_sql = "SELECT S.id, S.s_module  FROM S INNER JOIN L ON S.belong_id = L.id  AND S.is_old_module = 0  AND S.have_export = 1 AND S.belong_id =  '" + module1_id + "'"
            # 数据库连接
            data2 = db_connect(second_navigate_sql)
            for item in data2:
                module2_id = str(item[0])
                module2_name = str(item[1])
                # 二级导航栏点击
                module2_name = change_second_navigate(module1_name, module2_name, self.driver)
                # 查询tab栏
                tab_sql = "SELECT T.tab FROM T INNER JOIN S ON T.have_export = 1 AND T.belong_id = '" + module2_id + "' GROUP BY T.id"
                data3 = db_connect(tab_sql)
                tab_list = ''
                for item in data3:
                    tab_list = tab_list + str(item[0]) + ' '
                tab_list = delete_blank(str(tab_list).split(' '))
                # 切换tab栏，点击导出按钮
                if len(tab_list):
                    for i in range(len(tab_list)):
                        tab_name = change_table(tab_list[i], self.driver)
                        # 导出照片、导出
                        Export(self.driver, self.logger).new_Export(tab_name)
                else:
                    # 导出照片、导出
                    Export(self.driver, self.logger).new_Export(module2_name)
            # 页面刷新到首页
            go_Homepage(self.driver, self.logger)
