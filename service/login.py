from page_object.login_page import LoginPage


class TestLogin(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def test_login(self):
        login_Page = LoginPage(self.driver, self.logger)
        login_Page.get_url()
        login_Page.input_company()
        login_Page.input_account()
        login_Page.input_password()
        login_Page.click_login()
        login_Page.login_wait()
