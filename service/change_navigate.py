import time
from selenium.webdriver.common.by import By
from frame.iframe_skip import iframe_skip
from frame.is_element_exist import IsElementExist
from frame.logger import Logger


# 导航栏数据处理
# 导航栏切换iframe
def change_first_navigate(module_list, driver):
    module_name = ''
    iee = IsElementExist(driver)
    module_name = module_list
    if iee.is_element_exist(By.LINK_TEXT, str(module_name)):
        driver.find_element(By.LINK_TEXT, str(module_name)).click()
        time.sleep(1)
    else:
        print('导航栏' + str(module_name) + '不存在')
    # iframe跳转，重构后的模块偶数行下不需要切换iframe
    iframe_skip.iframe_enter(driver)
    return module_name


def change_second_navigate(module_list1, module_list2, driver):
    iee = IsElementExist(driver)
    module_name = module_list2
    if module_list1 == module_list2:
        if iee.is_element_exist(By.LINK_TEXT, module_name):
            driver.find_elements(By.LINK_TEXT, module_name)[1].click()
            time.sleep(1)
        else:
            print('导航栏' + module_list1 + '不存在')
    else:
        if iee.is_element_exist(By.LINK_TEXT, module_name):
            driver.find_element(By.LINK_TEXT, module_name).click()
            time.sleep(1)
        else:
            print('导航栏' + module_name + '不存在')
    # iframe跳转，重构后的模块偶数行下不需要切换iframe
    iframe_skip.iframe_enter(driver)
    return module_name
