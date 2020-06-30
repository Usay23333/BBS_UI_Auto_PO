# coding=utf-8

import pymysql
from utils.ConfigUtil import ConfigReader

class MysqlUtil():

    def __init__(self, dbname):
        self.cr = ConfigReader()
        self.__db = pymysql.connect(
            host = self.cr.get_db('host'),
            port = int(self.cr.get_db('port')),
            user = self.cr.get_db('user'),
            password = self.cr.get_db('password'),
            database = dbname,
            charset = self.cr.get_db('charset')
        )
        self.__cursor = self.__db.cursor()

    def get_cursor(self):
        return self.__cursor

    def select_all(self, sql):
        try:
            self.__cursor.execute(sql)
        except:
            return None
        return self.__cursor.fetchall()

    def select_one(self, sql):
        try:
            self.__cursor.execute(sql)
        except:
            return None
        return self.__cursor.fetchone()

    def execute(self, *sql):
        flag = False
        try:
            for i in sql:
                self.__cursor.execute(i)
            self.__db.commit()
            flag = True
        except:
            self.__db.rollback()
        finally:
            self.__db.close()
            return flag

    def close_cursor(self):
        self.__cursor.close()

    def close(self):
        self.__db.close()

    # def __del__(self):
    #     self.__db.close()

if __name__ == "__main__":
    # print(MysqlUtil('bbs').select_all("select username from pre_common_member where uid < 15 and username like 'user%'"))
    print(MysqlUtil('bbs').execute("update pre_common_member set password = 'second' where uid between 15 and 20", "update pre_common_member set password = 'first' where uid < 15 and username like 'user%'"))
    print(
        MysqlUtil('bbs').select_all("select password from pre_common_member where uid < 15 and username like 'user%'"))