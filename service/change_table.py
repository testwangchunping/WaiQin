import time
from selenium.webdriver.common.by import By
from frame.iframe_skip import iframe_skip
from frame.is_element_exist import IsElementExist


def change_table(mlist, i, driver):
    module_name = mlist[i]
    element = IsElementExist(driver).is_element_exist(By.LINK_TEXT, module_name)
    if element:
        driver.find_element(By.LINK_TEXT, module_name).click()
    else:
        print('tab栏' + module_name + '不存在或配置错误！')

    # 重构后模块tab后有iframe切换
    iframe_skip.iframe_enter(driver)
    time.sleep(1)
    return module_name
