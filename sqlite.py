#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class HyDataBase:
    # 连接数据库
    # 创建cusor
    def __init__(self,dbname):    
        self.conn = sqlite3.connect(dbname)    
        self.c = self.conn.cursor()

    # 创建表
    def createTable(self,create):    
        self.c.execute(create)

    # INSERT操作
    def insertData(self,insert):    
        self.c.execute(insert)
    
    # UPDATE操作
    def updateData(self,update):
        self.c.execute(update)
    
    # SELECT操作
    def selectData(self,select):
        self.cursor = self.c.execute(select)
        for row in self.cursor:
            print(row)

    # DELETE操作
    def deleteData(self,delete):
        self.c.execute(delete)


    # 提交当前事务
    def commitData(self):
        self.conn.commit()
    
    # 关闭数据库连接
    def closeDB(self):
        self.conn.close()


if __name__ == '__main__':    
    mydb = HyDataBase('testDB.db')
    print('数据库实例化成功，并且已连接数据库并创建cursor')
    mydb.createTable('CREATE TABLE COMPANY (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL);')
    print('创建COMPANY表成功')
    mydb.insertData("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
    mydb.insertData("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
    mydb.insertData("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
    mydb.insertData("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond', 65000.00 )")
    print('插入数据成功')
    mydb.selectData("select * from COMPANY;")
    print('select数据内容')
    mydb.updateData("UPDATE COMPANY set SALARY = 25000.00 where ID=1;")
    print('修改COMPANY数据表中ID为1的SALARY值')
    mydb.selectData("select * from COMPANY;")
    print('select数据内容')
    mydb.deleteData("DELETE from COMPANY where ID=2;")
    print('删除COMPANY数据表中ID为2的行')
    mydb.selectData("select * from COMPANY;")
    print('select数据内容')
    mydb.commitData()
    print('提交当前事务')
    mydb.closeDB()
    print('关闭数据库连接')
