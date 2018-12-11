from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def webElementWait(driver, type, error_tips):
    # webdriver 显示等待：WebDriverWait
    message = WebDriverWait(driver, 30, 1, None).until(
        EC.presence_of_element_located((type, error_tips)))
    tips = message.text
    return tips


def webElementWait_repeat(driver, type, error_tips):
    tips = ''
    try:
        # webdriver 显示等待：WebDriverWait
        message = WebDriverWait(driver, 5, 0.1, None).until(
            EC.presence_of_element_located((type, error_tips)))
        tips = message.text
        # print('已找到元素'+tips)
    except:
        # print('未找到元素')
        pass
    return tips
