import pymysql
from selenium.webdriver.common.by import By
from frame.webElementWait import webElementWait
from frame.DB_Connect import db_connect


class LoginPage(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    company_name = (By.NAME, 'company')
    account_name = (By.NAME, 'account')
    password_name = (By.NAME, 'pass')
    login_button = (By.CLASS_NAME, 'login_btn')

    server = input('请输入需要测试的服务器：cms/cms3/cms5/cms7/cs,并点击enter执行测试任务:')
    sql = "SELECT * from URL where server = '" + str(server) + "' "
    data = db_connect(sql)
    for item in data:
        f5_url = item[1]
        login_url = item[0]
        company = item[2]
        account = item[3]
        password = item[4]

    def get_url(self):
        self.driver.get(self.login_url)

    def input_company(self):
        self.driver.find_element(*self.company_name).send_keys(self.company)

    def input_account(self):
        self.driver.find_element(*self.account_name).send_keys(self.account)

    def input_password(self):
        self.driver.find_element(*self.password_name).send_keys(self.password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login_wait(self):
        try:
            # webdriver显示等待：webElementWait
            tips = webElementWait(self.driver, By.CLASS_NAME, self.error_tips)
            self.logger.debug(tips)
            self.logger.info('登陆失败')
        except:
            pass
