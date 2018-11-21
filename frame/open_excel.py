import xlrd


# 打开excel文件的具体sheet
def open_excel(file_path, sheet_name):
    # 打开文件
    workbook = xlrd.open_workbook(file_path)
    # 定位到指定sheet
    DataSheet = workbook.sheet_by_name(sheet_name)
    return DataSheet
