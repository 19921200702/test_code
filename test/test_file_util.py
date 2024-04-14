'''
针对file_util.py内的方法做单元测试
'''
import os
from unittest import TestCase

from util import file_util
class TestFileUtil(TestCase):
    def setUp(self) -> None:
        # 获取当前工程的跟目录
        self.project_root_path = os.path.dirname(os.getcwd())
    def test_get_dir_files_list(self):
        test_path = f'{self.project_root_path}/test/test_dir'
        result = file_util.get_dir_files_list(test_path,recursion=False)
        names = []   #定义一个list记录结果的文件名
        for i in result:
            names.append(os.path.basename(i))  # 可以从路径中取出最后的路径名
        # 为了避免结果的顺序产生测试失败，将names对象升序
        names.sort()
        self.assertEqual(['1','2'],names)
    # 在测试递归
        result = file_util.get_dir_files_list(test_path, recursion=True)
        names = []  # 定义一个list记录结果的文件名
        for i in result:
            names.append(os.path.basename(i))  # 可以从路径中取出最后的路径名
        names.sort()
        self.assertEqual(['1', '2','3','4','5'], names)
    def test_new_by_compare_lists(self):
        """测试new_by_compare_lists方法"""
        a_list = ['e:/a.txt','e:/b.txt']
        b_list = ['e:/a.txt','e:/b.txt','e/c.txt','e:/d.txt']
        result = file_util.get_new_by_compare_lists(a_list,b_list)
        self.assertEqual(['e/c.txt','e:/d.txt'],result)
