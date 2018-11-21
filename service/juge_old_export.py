from frame.is_element_exist import IsElementExist
from service.export import Export
from selenium.webdriver.common.by import By


class JugeOldExport(object):
    def __init__(self, driver, logger, module_name):
        self.driver = driver
        self.logger = logger
        self.module_name = module_name

    # 导出按钮id
    export_id = (By.ID, 'Export')
    export_photo_id = (By.ID, 'Export_photo')

    def juge_old_export(self):
        iee = IsElementExist(self.driver)
        if iee.is_element_exist(*self.export_id):
            Export(self.driver, self.logger).old_export(self.module_name)
        else:
            pass
        if iee.is_element_exist(*self.export_photo_id):
            Export(self.driver, self.logger).old_export_photo(self.module_name)
        else:
            pass
