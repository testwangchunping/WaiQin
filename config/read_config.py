import configparser
import os


class ReadConfigFile(object):
    # 登陆
    file_path = os.path.abspath('./config/config.ini')
    config = configparser.ConfigParser()

    config.read(file_path, encoding='utf-8-sig')

    # 读取文件目录
    port_data_filepath = config.get('filePath', 'port_data_filepath')

    new_export_sheet = config.get('filePath', 'new_export_sheet')
    new_export_sheet1 = config.get('filePath', 'new_export_sheet1')

    old_export_sheet = config.get('filePath', 'old_export_sheet')
    old_export_sheet1 = config.get('filePath', 'old_export_sheet1')

    new_import_sheet = config.get('filePath', 'new_import_sheet')
    new_import_sheet1 = config.get('filePath', 'new_import_sheet1')

    old_import_sheet = config.get('filePath', 'old_import_sheet')
    old_import_sheet1 = config.get('filePath', 'old_import_sheet1')

    import_data_filepath = config.get('filePath', 'import_data_filepath')
    chrome_path = config.get('filePath', 'chrome_path')
    fire_path = config.get('filePath', 'fire_path')
    ie_path = config.get('filePath', 'ie_path')

    log_path = config.get('filePath', 'log_path')

    screenshot_path = config.get('filePath', 'screenshot_path')
    report_path = config.get('filePath', 'report_path')
    testcase_path = config.get('filePath', 'testcase_path')
