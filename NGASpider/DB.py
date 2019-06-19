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
        values = (topic.title,
                  topic.url,
                  topic.create_time,
                  topic.reply_time,
                  topic.reply)
        cursor = self.connection.cursor()
        insert = ''' INSERT INTO topic
        (title, url, create_time, reply_time, reply)
        VALUES
        (%s, %s, %s, %s, %s)'''
        cursor.execute(insert, values)

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
    title VARCHAR(100),
    url VARCHAR(100),
    craete_time VARCHAR(100),
    reply_time VARCHAR(100),
    reply VARCHAR(100),
    PRIMARY KEY(topic_id)
    )
    '''
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
