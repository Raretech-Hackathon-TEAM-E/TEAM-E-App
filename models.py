import pymysql
from util.DB import DB


# サインアップ機能のDB接続操作

class dbConnect:
    def createUser(user):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email, password) VALUES(%s, %s, %s, %s);"
            cur.execute(sql,(user.uid,user.name, user.email, user.password))
            conn.commit()

        except Exception as e:
            print(e + 'が発生しています')
            return
        finally:
            cur.close()

# 
    
    def getUserID(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT uid FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            id = cur.fetchone()
            return id
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close


    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close