from frame.DB_Connect import db_connect
from frame.delete_blank import delete_blank

# print('测试输出！！！！')
#
# # 打开数据库连接
# db = pymysql.connect("120.79.190.131", "root", "password", "waiqin_demo")
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
# # 使用execute 方法执行SQL语句
# cursor.execute('select * FROM menu_tab WHERE first_tab = "出库管理"')
# # 使用fetchall()方法获取一行数据
# data = cursor.fetchall()
# for item in data:
#     module_end = ''
#     modulelist3 = ''
#     for i in range(len(item)-1):
#         modulelist3 = modulelist3 + str(item[i+1]) + ','
#     modulelist3 = modulelist3.split(',')
#     print(modulelist3)
#     module_end = delete_blank(modulelist3)
#     print(module_end)
#
# # 关闭数据库连接
# db.close()
# sql = "SELECT L.l_module, S.s_module, T.tab  FROM S INNER JOIN T ON T.belong_id = S.id INNER JOIN L ON S.belong_id = L.id  WHERE l_module = '库存管理'"
# # sql1 = 'select * FROM menu_tab WHERE first_tab = "出库管理"'
# sql2 = "select s_module from %s",sql
# data = db_connect(sql2)
# print(data)
# sql = "SELECT * from URL where server = 'cms1' "
# data = db_connect(sql)
# for item in data:
#     f5_url = item[1]
#
# print(f5_url)
#
# sql = "SELECT L.l_module, S.s_module, T.tab FROM S INNER JOIN T ON T.belong_id = S.id INNER JOIN L ON S.belong_id = L.id AND L.is_old_module = 0 ORDER BY L.id"
# data = db_connect(sql)
# for item in data:
#     print(item)
#     module_list1 = (str(item[0]) + ' ' + str(item[1])).split(' ')  # 一级导航栏、二级导航栏
#     module_list2 = str(item[2])  # tab栏
#
#     module_list2=[module_list2]
#     print(module_list2)
#     print(len(module_list2))

# http://cms.xiaobuwq.com/wq/admin/core/login/index
# http://cms.xiaobuwq.com/wq/admin/core/index/index
# current_url = 'http://cms.xiaobuwq.com/wq/admin/core/app/iframe?_is_for_nav=1&_app_action=%2Fuser&_nav_name=%E5%91%98%E5%B7%A5%E7%AE%A1%E7%90%86'
# f5_url = current_url.split('core')[0]+'core/index/index'
# print(f5_url)
# 查询第一级导航栏
# sql = "SELECT L.id,L.l_module FROM L WHERE L.is_old_module = 0 ORDER BY L.id"
# # 数据库连接
# data = db_connect(sql)
# for item in data:
#     print(str(item[0])+','+item[1])

# 查询第一级导航栏
sql = "SELECT L.id, L.l_module  FROM L WHERE L.is_old_module = 0 AND L.id = 11  ORDER BY L.id"
# 数据库连接
data = db_connect(sql)
for item in data:
    # self.logger.info(str(item[0]))
    # self.logger.info(item[1])
    module1_id = str(item[0])
    module1_name = item[1]
    print(module1_id)
    print(module1_name)
    # module1_name = change_navigate(module1_name, self.driver)
    # 查询第二级导航栏
    SQL2 = "SELECT S.id, S.s_module FROM S INNER JOIN L ON S.belong_id = L.id AND S.belong_id =  '"+ module1_id +"'"
    # 数据库连接
    data1 = db_connect(SQL2)
    for item in data1:
        module2_id = str(item[0])
        module2_name = str(item[1])
        # module2_name = change_navigate(module2_name, self.driver)
        print(module2_id + ',' + module2_name)
        SQL3 = "SELECT T.tab FROM T INNER JOIN S ON T.belong_id = '"+ module2_id +"'GROUP BY T.id"
        data2 = db_connect(SQL3)
        tab_list=''
        for item in data2:
            tab_list = tab_list+str(item[0])+' '
        tab_list=delete_blank(str(tab_list).split(' '))
        print(tab_list)
        if len(tab_list):
            print('有table项')
        else:
            print('无table项')

