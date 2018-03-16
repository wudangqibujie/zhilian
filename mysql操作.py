import pymysql
conn = pymysql.Connect(host="127.0.0.1",port = 3306,user = "root",passwd = "Ljj281150",db = "win_test")
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
#FETCHONE()是获取单挑数据
data = cursor.fetchone()
print(data)
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

sql = "SELECT * FROM EMPLOYEE"
cursor.execute(sql)
result = cursor.fetchall()
print(result)


conn.close()

