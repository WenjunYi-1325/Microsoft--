from mysql_helper import MySqlHelper

db = MySqlHelper()

# 1. 增加
db.execute(
    "INSERT INTO student VALUES(%s,%s,%s)",
    (5, "Alex", 198)
)

# 2. 查询
result = db.query_all("SELECT * FROM student")
print("增加后的数据：")
print(result)

# 3. 修改
db.execute(
    "UPDATE student SET height=%s WHERE id=%s",
    (175, 3)
)

# 4. 查询
result = db.query_one(
    "SELECT * FROM student WHERE id=%s",
    (3,)
)
print("修改后的：")
print(result)

# 5. 删除
db.execute(
    "DELETE FROM student WHERE id=%s",
    (5,)
)

# 6. 查询
result = db.query_all("SELECT * FROM student")
print("删除后的数据：")
print(result)

db.close()