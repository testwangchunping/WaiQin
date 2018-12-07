from page_object.login_page import LoginPage


# 页面刷新到首页
def go_Homepage(driver, logger):
    f5_url = 'http://' + LoginPage.server + '.xiaobuwq.com/wq/admin/core/index/index'
    driver.get(f5_url)
