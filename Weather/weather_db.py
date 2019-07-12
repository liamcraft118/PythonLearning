# -*- coding: utf-8 -*-

from db import DB


class weather_db(DB):

    def connect(self):
        self.conn = self._connect('weather')

    def insert_daily_weather(self, info):
        sql = '''INSERT INTO daily_weather
        (date_formatted, day_code, day_text, night_code, night_text, temp_high, temp_low)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s) '''
        cursor = self.conn.cursor()
        cursor.execute(sql, info)

    def fetch_latest_weather(self):
        sql = '''SELECT * from daily_weather ORDER BY id DESC LIMIT 1;'''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        info = cursor.fetchone()
        return info
