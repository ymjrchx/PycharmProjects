'''
Created on 2018年10月10日

@author: Administrator
'''
import pymysql as pm

conn = pm.connect("localhost", "root", "123456", "swt_one")
cursor = conn.cursor()
cursor.execute("select * from actlist")
emp = cursor.fetchone()
print(emp)
print(type(emp))
all = cursor.fetchall()
print(all)
conn.close()

if __name__ == '__main__':
    pass