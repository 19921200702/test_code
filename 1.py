# print('hello world')
import os

def get_dir_files_list(path='/',recursion=False):
    dir_names = os.listdir(path)
    files = []
    for dir_name in dir_names:
        absolute_path = f'{path}/{dir_name}'
        if not os.path.isdir(absolute_path):
            files.append(absolute_path)
        else:
            if recursion:
                recursion_file_list = get_dir_files_list(absolute_path,recursion=recursion)
                files += recursion_file_list
    return files


print(get_dir_files_list('F:/百度网盘下载/MySQL性能优化',recursion=True))
print(os.path.dirname(os.getcwd()))
a = os.path.dirname(os.getcwd())
print(a)
print(os.path.basename(a))