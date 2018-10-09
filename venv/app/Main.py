import pymysql as sql
import  flask
conn=sql.connect(host='localhost',port=3306,user='root',password='root123',db='DbmsProject')
cursor=conn.cursor();
ans = cursor.execute("SELECT Password FROM examples where Username = 'admin'")
print(ans)
print(type(cursor
      .fetchall()[0][0]))


conn.close()