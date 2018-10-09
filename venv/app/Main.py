import pymysql as sql
import  flask
conn=sql.connect(host='localhost',port=3306,user='root',password='root123',db='DbmsProject')
cursor=conn.cursor();
cursor.execute("SELECT * FROM examples")
print(cursor
      .fetchall())



conn.close()