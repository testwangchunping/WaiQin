from selenium.webdriver.common.by import By
from config.read_config import ReadConfigFile
from frame.webElementWait import webElementWait


class LoginPage(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    company_name = (By.NAME, 'company')
    account_name = (By.NAME, 'account')
    password = (By.NAME, 'pass')
    login_button = (By.CLASS_NAME, 'login_btn')
    readConfig = ReadConfigFile()

    def get_url(self):
        self.driver.get(self.readConfig.login_url)

    def input_company(self):
        self.driver.find_element(*self.company_name).send_keys(self.readConfig.U_company)

    def input_account(self):
        self.driver.find_element(*self.account_name).send_keys(self.readConfig.U_account)

    def input_password(self):
        self.driver.find_element(*self.password).send_keys(self.readConfig.U_password)

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
