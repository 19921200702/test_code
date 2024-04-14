# sql1 = "insert into table(name) values (NULL)"
# sql2 = "a" + "b" + "c"
# v = "NULL"
# sql3 = "insert into table(name) values (" + v + ")"
# name = "张" + "三"
# print(name)
# print(sql3)
# sql = f"insert into table(name) values ({})"
from config import project_config as conf
sql = f"INSERT IGNORE INTO {conf.target_orders_detail_table_name}(" \
      f"order_id,barcode,name,count,price_per,retail_price,trade_price,category_id,unit_id) VALUES"
print(sql)

