import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class NewPlayer:

    def __init__(self, user_id, user_name, date):

        self.user_id = user_id
        self.user_name = user_name
        self.creation_date = date

        db = MySQLdb.connect(user=USERDATABASE, passwd=PASSWORDDATABASE, host="localhost", db=DATABASE)#connexion
        cursor = db.cursor() #création du cursor
        sql = f""
        cursor.execute(sql) #fonction sql
        db.commit()
        db.close()