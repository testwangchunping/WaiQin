from frame.screenshoot import get_window_img
import sys


def view_screenshots(self, logger, func_name, pic_num=0):
    name = sys._getframe().f_code.co_name
    func_name.pic_num = pic_num + 1
    print('用例数量' + str(func_name.pic_num))
    get_window_img(self, logger, name, str(func_name.pic_num))  # 最后一项为图片第几张
