'''
和文件处理相关的方法，都定义到这个python文件中
'''
import os
# files = []
def get_dir_files_list(path='./',recursion=False):
    files = []
    dir_names = os.listdir(path)
    # print(dir_names)
# get_dir_files_list('F:/百度网盘下载/4-ETL/Day01/数据资料/JSON数据（订单业务）')

    for dir_name in dir_names:
        absolute_path = f'{path}/{dir_name}'
        if not os.path.isdir(absolute_path):
            files.append(absolute_path)
        else:
            if recursion:
                recursion_file_list = get_dir_files_list(absolute_path,recursion=recursion)
                files += recursion_file_list
    return files
def get_new_by_compare_lists(a_list,b_list):
    """
    从两个list中进行对比
    找出：B中有的而 A中没有的
    比如：
    A：[1]
    B:[1,2,3]
    结果是：[2,3]
    :param a_list:A数据集
    :param b_list:B数据集
    :return: list 存放B中有的而A中没有的数据
    """
    # 创建一个空list，用来存放结果集
    new_list = []

    # 开始进行对比，for循环B数据集，验证B数据集中的数据，是否在A里面存在
    for i in b_list:
        if i not in a_list:
            new_list.append(i)
    return new_list



# print(get_dir_files_list('F:/Star Rail',recursion=True))
# l = get_dir_files_list('F:/百度网盘下载/4-ETL/Day01/数据资料/JSON数据（订单业务）/aa',recursion=True)
# print(l)
