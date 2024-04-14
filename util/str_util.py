# coding:utf8
"""
专用于字符串的相关工具代码
"""
def check_null(data):
    """
    检查传入的字符串，是否为无意义内容，如果是就返回True,否则返回False
    无意义：字符串为空字符串，内容是None，内容是null,内容是undefined
    :param data:传入的被检查的字符串内容
    :return:True 无意义，False有意义
    """
    if not data:
        # data这个对象，真的是None 直接返回无意义
        return True
    # 统一转小写，避免大小写问题
    # 调用字符串的lower（）方法，将字符串转换为全小写
    data = data.lower()
    # 判断是否无意义
    if data == "none" or data == "" or data == "null" or data == "undefined":
        # 满足任意一个条件，就是无意义，返回True
        return True
    return False
def check_str_null_and_transform_to_sql_null(data):
    """
    检查字符串，如果是空内容，就返回SQL意义上的NULL(插入的SQl语句中会插入真正的NULL)
    如果是有意义的内容，返回'内容本身'
    :param data:
    :return:
    """
    if check_null(str(data)):
        # 如果进入if，表示内容无意义，返回SQL意义上的NULL
        return "NULL"
    else:
        # 内容有意义，返回内容本身
        return f"'{data}'"

def check_number_null_and_transform_to_sql_null(data):
    """
     检查数字，如果是空内容，就返回SQL意义上的NULL(插入的SQl语句中会插入真正的NULL)
    如果是有意义的内容，返回内容本身
    :param data:
    :return:
    :param data:
    :return:
    """
    if data and not check_null(str(data)):
        # and 两个是True才能进来if
        # data如果不是None,而是有内容，那么就能进来
        # 同时not check_null(str(data)是True 才能进来
        # 也就是 check_null(str(data))是False, 表示有意义
        # 总结：必须满足data有内容，（不是None）同时满足data的内容有意义才会进入if
        return data
    else:
        # 这个数据有问题
        return "NULL"      # return SQl意义上的NULL





def clean_str(data):
    if check_null(data):
        # 如果是无意义的内容，比如字符串None,字符串Null 等, 这些不影响插入操作不理会
        return data
    # 如果有意义的内容，需要处理，比如： 可口可乐\ 内容中自带斜杠导致程序出错
    # 乱七八糟的符号，我们要处理掉
    data = data.replace("'", "")
    data = data.replace('"', "")
    data = data.replace("\\", "")
    data = data.replace(";", "")
    data = data.replace(",", "")
    data = data.replace("@", "")
    return data



