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
            return None
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
            cur.close()


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
            cur.close()


# 全チャンネル名の取得

    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()

# チャンネルIDの取得



























































#チャンネル名の取得

def getChannelByName(channel_name):
    try:
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "SELECT * FROM channels WHERE name=%s;"
        cur.execute(sql, (channel_name))
        channel = cur.fetchone()
        return channel
    except Exception as e:
        print(e + 'が発生しています')
        return None
    finally:
        cur.close()


#チャンネルの追加
def addChannel(uid, newChannelName, newChannelDescription):
    try:
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "INSERT INTO channels (uid, channel_name, abstract) VALUES (%s, %s, %s);"
        cur.execute(sql, (uid, newChannelName, newChannelDescription))
        conn.commit()
    except Exception as e:
        print(e + 'が発生しています')
        return None
    finally:
        cur.close()