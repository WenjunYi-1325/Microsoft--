import pymysql

class MySqlHelper:

    def __init__(self, host="localhost", user="root", password="", database="study"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
        # 建立连接
        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset="utf8"
        )
        
        self.cursor = self.conn.cursor()

    def execute(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
            return True
        
        except Exception as e:
            self.conn.rollback()
            print("执行失败：", e)
            return False

    def query_all(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Exception as e:
            print("查询失败：", e)
            return []

    def query_one(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchone()
        except Exception as e:
            print("查询失败：", e)
            return None
        
    def close(self):
        self.cursor.close()
        self.conn.close()