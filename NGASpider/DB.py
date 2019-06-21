# -*- coding: utf-8 -*-

import pymysql


class DB(object):
    connection = None

    def connect(self):
        self.connection = pymysql.connect(host='localhost',
                                          port=3306,
                                          user='root',
                                          password='1234!@#$',
                                          db='nga_wszt',
                                          charset='utf8')

    def insert(self, topic):
        cursor = self.connection.cursor()
        insert = ''' INSERT INTO topic
        (title, author_name, author_id, replyer, reply_count, create_time)
        VALUES
        (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(insert, topic)

    def commit(self):
        self.connection.commit()

    def readAllTitle(self):
        select = '''
        SELECT title FROM topic
        '''
        cursor = self.connection.cursor()
        cursor.execute(select)
        result = cursor.fetchall()
        return result


if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='1234!@#$',
                                 db='nga_wszt',
                                 charset='utf8')
    sql = '''
    CREATE TABLE IF NOT EXISTS topic(
    topic_id INT AUTO_INCREMENT,
    title VARCHAR(255),
    author_name VARCHAR(255),
    author_id VARCHAR(255),
    replyer VARCHAR(255),
    reply_count VARCHAR(255),
    create_time VARCHAR(255),
    PRIMARY KEY(topic_id)
    )
    '''
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
