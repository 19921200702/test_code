from unittest import TestCase
from util.mysql_util import MySQLUtil,get_processed_files
from config import project_config as conf
# 要继承TestCase
class TestMySQLUtil(TestCase):
    def setUp(self) -> None:
        # setUp等同于 __init__
        self.db_util = MySQLUtil()
    def test_query(self):
        # 测试MySQLUtil中的query方法
        # 不使用mysql中已存在的表，解耦合，确保单元测试的独立性
        # 耦合：和其它的东西关联的太深
        # 解耦合：解除和其它的东西的深度关联，确保自身的独立
        # 要自己建个表，自己插入数据，使用被测试的query来验证它
        self.db_util.select_db('test')
        self.db_util.check_table_exists_and_create(
            'test',
            'for_unit_test',
            'id int primary key ,name varchar(255)'
        )
        self.db_util.execute("truncate for_unit_test")
        self.db_util.execute(
            "insert into for_unit_test values (1,'潇潇'),(2,'甜甜')"
        )
        # 数据集准备好了，进行查询
        result = self.db_util.querry("select * from for_unit_test order by id")
        expected = ((1,'潇潇'),(2,'甜甜'))
        self.assertEqual(expected,result)
        # # 清理单元测试的残留
        self.db_util.execute("drop table for_unit_test")
        self.db_util.close_conn()
    # def test_execute_without_autocommit(self):
    #     # 设置autocommit为True
    #     self.db_util.conn.autocommit(True)
    #     self.db_util.select_db('test')
    #     self.db_util.check_table_exists_and_create(
    #         'test',
    #         'for_unit_test',
    #         'id int primary key ,name varchar(255)'
    #     )
    #     self.db_util.execute("truncate for_unit_test")
    #     self.db_util.execute_without_autocommit(
    #         "insert into for_unit_test values (1,'潇潇')"
    #     )
    #     # 数据集准备好了，进行查询
    #     result = self.db_util.querry("select * from for_unit_test order by id")
    #     expected = ((1, '潇潇'))
    #     self.assertEqual(expected, result)
    #     # # 清理单元测试的残留
    #     # 设置autocommit为false
    #     self.db_util.conn.autocommit(False)
    #     self.db_util.execute_without_autocommit(
    #         "insert into for_unit_test values (2,'甜甜')"
    #     )
    #
    def test_get_processed_files(self):
        '''
        测试获取已经被处理过的文件列表功能的单元测试
        保证独立性，自备表和数据
        '''
        self.db_util.select_db("test")
        self.db_util.check_table_exists_and_create(
            "test",
            "test_file_monitor",
            conf.metadata_file_monitor_table_create_cols
        )
        self.db_util.execute("truncate test_file_monitor")
        # 准备测试数据
        # self.db_util.execute(f'''
        #     insert into {conf.metadata_file_monitor_table_name} values (9999999,'testfile',1024,'2000-01-01 10:00:00')
        #     ''')
        self.db_util.execute(
            '''
            insert into test_file_monitor values (1,'e:/a.txt',1024,'2000-01-01 10:00:00')
            '''
        )
        # 执行查询结果
        result = get_processed_files(self.db_util,db_name="test",table_name="test_file_monitor")

        # print(result)
        self.assertEqual(["e:/a.txt"] , result)
        # 清理痕迹
        self.db_util.execute("drop table test_file_monitor")
        self.db_util.close_conn()

