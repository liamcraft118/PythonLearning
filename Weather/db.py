# -*- coding: utf-8 -*-


import pymysql


class DB:
    def _connect(self, db):
        try:
            conn = pymysql.connect(host='localhost',
                                   port=3306,
                                   user='root',
                                   password='1234!@#$',
                                   db=db,
                                   charset='utf8')
        except pymysql.DatabaseError as e:
            print(e)
            with open('error.log', 'w') as file:
                file.write(e)
                file.close
            return None
        else:
            return conn

    def connect(self):
        return None

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
