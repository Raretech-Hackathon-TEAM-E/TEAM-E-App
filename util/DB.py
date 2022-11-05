import pymysql

# DBとPythonをつなぐ初期設定を行う（models.pyに継承する親クラスの設定）
# 接続に失敗した際の例外処理を記述

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="localhost",
            db="chatapp",
            user="testuser",
            password="testuser",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
