# coding=utf-8
import os
import time
from selenium.webdriver.common.by import By
from config.read_config import ReadConfigFile
from frame.iframe_skip import iframe_skip
from frame.is_element_exist import IsElementExist
from frame.webElementWait import webElementWait


class WqImport(object):
    def __init__(self, driver, logger, module_name):
        self.driver = driver
        self.logger = logger
        self.module_name = module_name

    # import_module_name,导入文件应该以模块名命名规则
    # 1、列表中无table切换，导入文件名为“最后一个link_text导航栏名”；
    # 2、列表中有table切换，导入文件名为“切换的table的名字”）

    # 导入失败的提示
    error_message = '没有可导入的文件、导入文件名错误、导入失败或请求超时'
    readConfig = ReadConfigFile()
    file_path = readConfig.import_data_filepath
    # 导入按钮
    import_button_group = 'more-select-box-ipt_client_climanage_import_button_group'  # 客户管理组合导入按钮
    import_text = '导入'  # 普通导入按钮

    # 文件上传按钮
    import_file_button1 = (By.ID, 'upload-file')  # xls格式文件
    import_file_button2 = (By.NAME, 'file')  # zip格式文件
    # 确认导入按钮
    confirm_button1 = (By.ID, 'OK-Button')  # xls格式文件
    confirm_button2 = (By.ID, 'save_button')  # zip格式文件
    # 导入成功的提示
    import_success_message = '//*[@id="task_body"]/div/div[1]/span[1]'
    # 导入成功后，返回上一级按钮
    import_success_button = (By.XPATH, '//*[@id="task_body"]/div/div[1]/a')
    # 返回上级按钮
    return_button = (By.CLASS_NAME, 'btn_back')

    # 点击导入按钮后的操作
    def import_back(self, number, import_content):
        # iframe跳转
        iframe_skip.iframe_enter(self.driver)
        # 判断导入文件类型
        time.sleep(2)
        try:
            filetext = self.driver.find_element(By.XPATH, '//*[@id="adminForm"]/div[2]/div[1]').text
        except:
            filetext = self.driver.find_element(By.XPATH, '//*[@id="upfile_form"]/div[2]/div[1]').text
            # 文件类型
        if 'Excel' in filetext:
            filetype = '.xls'
        else:
            filetype = '.zip'
        # 获取待导入文件
        if number == 1:
            import_file = self.file_path + self.module_name + filetype
        else:
            import_file = self.file_path + self.module_name + str(self.id + 1) + filetype
        try:
            # xls类型文件上传
            self.driver.find_element(*self.import_file_button1).send_keys(import_file)
            time.sleep(2)
            self.driver.find_element(*self.confirm_button1).click()
        except:
            # zip类型文件上传
            self.driver.find_element(*self.import_file_button2).send_keys(import_file)
            time.sleep(10)
            self.driver.find_element(*self.confirm_button2).click()
        try:
            # webdriver显示等待：webElementWait
            webElementWait(self.driver, By.XPATH, self.import_success_message)
            tips = self.driver.find_element(By.ID, 'main-container').text
            self.logger.info(self.module_name + '-->' + import_content + ':' + tips)
            self.driver.find_element(*self.import_success_button).click()
            self.driver.find_element(*self.return_button).click()
        except:
            self.logger.warning(self.module_name + '-->' + import_content + ':' + self.error_message)
            self.driver.find_element(*self.import_success_button).click()

    def test_old_import(self):
        iee = IsElementExist(self.driver)
        if iee.is_element_exist(By.PARTIAL_LINK_TEXT, self.import_text):
            element = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
            number = len(element)
            for self.id in range(number):
                time.sleep(2)
                element = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
                import_content = element[self.id].text
                element[self.id].click()
                time.sleep(2)
                self.import_back(number, import_content)
        else:
            pass

    def test_new_import(self):
        iee = IsElementExist(self.driver)
        # 组合导入按钮
        if iee.is_element_exist(By.CLASS_NAME, self.import_button_group):
            self.driver.find_element(By.CLASS_NAME, self.import_button_group).click()
            element = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
            number = len(element)
            # 刷新页面
            self.driver.refresh()
            time.sleep(3)
            for self.id in range(number):
                self.driver.find_element(By.CLASS_NAME, self.import_button_group).click()
                time.sleep(2)
                element = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
                import_content = element[self.id].text
                element[self.id].click()
                self.import_back(number, import_content)
        else:
            pass
        # 单个导入按钮
        if iee.is_element_exist(By.PARTIAL_LINK_TEXT, self.import_text):
            element = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
            number = len(element)
            for self.id in range(number):
                element = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
                import_content = element[self.id].text
                element[self.id].click()
                time.sleep(2)
                self.import_back(number, import_content)
        else:
            pass
