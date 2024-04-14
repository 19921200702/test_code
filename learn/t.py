# cols = '''
# id int primary key,
# name varchar(255),
# address varchar(255)
# '''
# table_name = 'stu'
# create_sql = f'CREATE TABLE {table_name}({cols})'
# print(create_sql)
# file = open('F:/a.txt','r')
# print('你好\n我好')
# class STU:
#     def __init__(self):
#         self.name = '张三'
#     def say_hello(self):
#         print(self.name)
# s = STU()
# s.say_hello()
# from util.mysql_util import MySQLUtil
# a = MySQLUtil()
# a.select_db('db_winfunc')
# print(a.querry("desc purchase"))
# result = a.querry("select avg(price) from purchase")
# print(result)

# process_files = []
# for r in result:
#     process_files.append(r[0])
# print(process_files)
# import re
#
# a = "1/2页 共13条数据"
# py = re.findall("(.*)页 共(.*)", a)
# print(py)
# for i in open("C:/Users/21977/Desktop/新建 文本文档.md","r",encoding="UTF-8"):
#     i = i.replace("\n","")
#     print(i)
import json
json_str1 = '{"name":"张三","age":11,"address":"北京市海dian区"}'
json_str2 = '{"name":"张三","age":11,"address":"北京市海dian区"}'
# json_dict = json.loads(json_str)
# print(json_dict['address'])
# 用模型承载数据，模型就是一个class，一个class的实例，就是一条数据
class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def to_csv(self,seq=","):
        return f"{self.name}{seq}{self.age}{seq}{self.address}"
    def generate_insert_sql(self):
        return f"insert into person values ('{self.name}','{self.age}','{self.address}')"


p1 = Person('张三',11,'北京市海定区')
p2 = Person('王五',13,'北京市昌平区')
print(p1.to_csv(";"))
print(p2.to_csv(";"))
print(p1.generate_insert_sql())
print(p2.generate_insert_sql())
