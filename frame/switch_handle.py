class SwitchHandle(object):
    def __init__(self, driver, Logger):
        self.driver = driver
        self.Logger = Logger

    def switch_handle(self):
        handles = self.driver.window_handles
        for i in handles:
            if i != self.driver.current_window_handle:
                self.driver.switch_to.window(i)
        self.Logger.debug('跳转到新的句柄')
