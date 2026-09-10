import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",   # 替换为你的 ASCII 密码
    database="study",
    charset="utf8"
)

print("连接成功！")
conn.close()