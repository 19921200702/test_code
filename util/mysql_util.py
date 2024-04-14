import pymysql
from config import project_config as conf
from util.logging_util import init_logger
logger = init_logger()
class MySQLUtil:
    def __init__(self, host=conf.metadata_host, user=conf.metadata_user,
                 password=conf.metadata_password, port=conf.metadata_port,
                 charset=conf.mysql_charset, autocommit=False):
        '''
        构建到MySQl的连接，默认去连接配置文件中配置的元数据，如果想要连接其它数据库，传参即可
        :param host:
        :param user:
        :param password:
        :param port:
        :param charset:
        :param autocommit:
        '''
        self.conn = pymysql.Connection(
            host=host,
            user=user,
            password=password,
            port=port,
            charset=charset,
            autocommit=autocommit

        )
    # 输出一条info级别的日志
        logger.info(f'构建完成到{host}:{port}的数据库连接...')
    def close_conn(self):
        if self.conn:
            self.conn.close()


    def querry(self,sql):
        '''
        执行指定的sql语句并返回查询结果
        :return:
        执行sql需要构建一个游标
        '''
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql)
        # 通过游标获取执行结果
        result = cursor.fetchall()
        # 关闭游标
        cursor.close()
        # 输出一份日志
        logger.info(f'执行查询的SQL语句完成，查询的结果有{len(result)}条，执行的SQL语句是:{sql}')

        return result
    def select_db(self,db):
        """
        选择数据库，就相当于sql中的use功能
        :param db:
        :return:
        """
        self.conn.select_db(db)
    def execute(self,sql):
        '''直接执行一条sql语句，不用去理会返回值'''
        # 拿到游标
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql)

        logger.debug(f'执行了一条SQL:{sql}')
        if not self.conn.get_autocommit():
            # 这里表示的是自动提交为false,然后会跳转到这个if控制的条件中
            self.conn.commit()
        cursor.close()
    def execute_without_autocommit(self,sql):
        '''
        直接执行一条sql语句，不理会返回值
        不会判断自动提交，只执行不会commit
        :param sql:
        :return:
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        logger.debug(f'执行了一条SQL:{sql}')

    def check_table_exists(self,db_name,table_name):
        '''
        检查给定的数据库下，给定的表，是否存在
        :param db_name:     被检查的数据库
        :param table_name:  被检查的表名字
        :return:          True存在，False不存在
        '''
        # 切换数据库
        self.conn.select_db(db_name)

        # 查询
        # SQL查询结果是 元组嵌套元组
        # 假设有两个表，table1和table2，比如show tables的结果
        # ((table1,),(table2,))
        result = self.querry("show tables")

        return (table_name, ) in result
    def check_table_exists_and_create(self,db_name,table_name,create_tools):
        '''
        检查表是否存在，如果不存在，就创建它
        :param db_name:     数据库名字
        :param table_name:  被创建的表名字
        :param create_tools:    建表语句的列信息
        :return:
        '''
        # 先判断表是否存在
        if not self.check_table_exists(db_name,table_name):
            # 进来if表示，表不存在

            # 准备建表的SQL语句
            create_sql = f'CREATE TABLE {table_name}({create_tools})'
            # 执行建表语句
            self.conn.select_db(db_name)
            self.execute(create_sql)

            logger.info(f'在数据库: {db_name}中创建了表: {table_name}完成。建表语句是: {create_sql}')
        else:
            logger.info(f'数据库:{db_name}中，表{table_name}已经存在，创建表的操作跳过。')
def get_processed_files(db_util,
                        db_name=conf.metadata_db_name,
                        table_name=conf.metadata_file_monitor_table_name,
                        create_cols = conf.metadata_file_monitor_table_create_cols):

    '''
    查询已经被处理过的文件列表
    通过被查询的表，如果不存在，那么会先创建它
    :param db_util:
    :return:
    '''

    # 已经处理过的数据的信息记录，我们存入到数据库：metadata
    # 存入到表：file_monitor中
    # comment 是mysql中的注释


    db_util.select_db(db_name)
    db_util.check_table_exists_and_create(
        db_name,  # 数据库名
        table_name,  # 表名
        create_cols  # 建表语句列信息
    )

    # current_timestamp 表示当前时间戳，如果设置为列的默认值，如果你插入数据不插入这个列的话，会自动填入当前的时间
    result = db_util.querry(f"select file_name from {table_name}")
    # # 将SQL查询结果 转化为list返回
    processed_files = []
    for r in result:
        processed_files.append(r[0])

    return processed_files

# util = MySQLUtil()
# print(util.check_table_exists('db_itheima', 'dage'))
# util.check_table_exists_and_create('db_itheima','stu2','id int primary key, name varchar(255)')
# util1 = MySQLUtil()
# util1.select_db('db_itheima')
# util1.check_table_exists_and_create('db_itheima',
#             'for_unit_test',
#             'id int primary key ,name varchar(255)')
# util1.execute('truncate for_unit_test')
# util1.execute("insert into for_unit_test values (1,'潇潇'),(2,'甜甜')")
# # util1.execute('insert into for_unit_test values(1,'潇潇')')