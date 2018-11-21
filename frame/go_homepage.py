from config.read_config import ReadConfigFile


# 页面刷新到首页
def go_Homepage(driver):
    readConfig = ReadConfigFile()
    driver.get(readConfig.f5_url)
