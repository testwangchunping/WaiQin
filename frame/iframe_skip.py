class iframe_skip(object):
    def iframe_enter(driver):
        iframe_name = 'app_iframe'
        try:
            driver.switch_to.frame(iframe_name)
        except:
            pass

    def iframe_exit(driver):
        try:
            driver.switch_to.default_content()
        except:
            pass
