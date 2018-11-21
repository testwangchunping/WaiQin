# coding=utf-8


class IsElementExist(object):
    def __init__(self, driver):
        self.driver = driver

    #   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    def is_element_exist(self, type, elements):

        try:
            self.driver.find_element(type, elements)
            return True
        except:
            return False

