#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

# 连接数据库
conn = sqlite3.connect('test.db')


# 创建cusor
c = conn.cursor()

# 创建表

c.execute("""CREATE TABLE COMPANY
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);""")



# INSERT操作
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (1, 'Paul', 32, 'California', 20000.00 )")

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (4, 'Mark', 25, 'Rich-Mond', 65000.00 )")


# UPDATE操作
c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")


# SELECT操作
cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
    print(row)

# DELETE操作
c.execute("DELETE from COMPANY where ID=2;")


# 提交当前事务
conn.commit()

# 关闭数据库连接
conn.close()
