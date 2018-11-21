def delete_blank(list):
    # 去掉字符串中的空格
    while '' in list:
        list.remove('')
    return list
