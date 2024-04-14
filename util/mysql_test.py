import pymysql
conn = pymysql.Connection(
host='localhost',
            user='root',
            password='root',
            port=3306,
            charset='utf8',
            autocommit=True
)
conn.select_db('db_itheima')
cursor = conn.cursor()
# cursor.execute('select * from class_attendance_app')
# cursor.execute("insert into xiaodi values (3,'二次元',1)")
# cursor.execute("insert into xiaodi values (4,'潇潇',1)")
# cursor.execute('select * from product')
# conn.commit()
# result = cursor.fetchall()
# for i in result:
#     print(i)
# cursor.execute("insert into for_unit_test values (1,'潇潇')")
cursor.execute("select * from dage ")
result = cursor.fetchall()
for i in result:
    print(i)