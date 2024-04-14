import pymysql
conn = pymysql.Connection(
    host='localhost',
    user='root',
    password='root',
    charset='utf8',
    autocommit=True
)
conn.select_db('db_winfunc')
cursor = conn.cursor()
cursor.execute('select * from department')
result = cursor.fetchall()
for i in result:
    print(i)