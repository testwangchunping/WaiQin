# coding=utf-8
# 保证程序能够在cmd运行
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from config.read_config import ReadConfigFile
import time
import unittest
from Tools.HTMLTestRunner_PY3 import HTMLTestRunner

readConfig = ReadConfigFile()
# 设置报告文件保存路径（绝对路径才能在cmd运行）
report_path = os.path.abspath(readConfig.report_path)
# 设置报告名
report_name = 'Report.html'
# 设置报告标题
report_title = '项目导入导出测试报告'
# 设置报告副标题
report_descibe = '用例测试情况'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = os.path.abspath(report_path) + now + report_name
# 通过open()方法以二进制写模式打开当前目录下的Report.html，如果没有，则自动创建该文件
fp = open(HtmlFile, "wb")

# discover找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到的文件才能被加载
# 跑testsuite包下所有测试用例,在实际脚本开发过程中，最后都采用这个方法来批量管理和执行几百上千的测试用例
# suite = unittest.TestLoader().discover(suites_path, pattern='test*.py')
# 设置用例路径
testcase_path = os.path.abspath(readConfig.testcase_path)
suite = unittest.TestLoader().discover(testcase_path, pattern='test_ex*.py')

if __name__ == '__main__':
    # 执行用例
    # 初始化一个HTMLTestRunner实例对象，用来生成报告（stream用来指定测试报告文件，title定义测试报告标题，description定义测试报告副标题）
    runner = HTMLTestRunner(stream=fp, title=report_title, description=report_descibe)
    # 开始执行测试套件中所组装的测试用例
    runner.run(suite)
    # 关闭报告文件
    fp.close()
