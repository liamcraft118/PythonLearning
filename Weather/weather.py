# -*- coding: utf-8 -*-

import requests
import json
from ding_robot import DingRobot


class Weather:
    def __init__(self):
        self.private_key = 'SD6IoDu-6GH8MHRes'
        self.location = 'chengdu'

    def life_suggestion(self):
        url = 'https://api.seniverse.com/v3/life/suggestion.json?key=%s&location=%s&language=zh-Hans' % (self.private_key, self.location)
        r = requests.get(url)
        return r.text

    def now(self):
        url = 'https://api.seniverse.com/v3/weather/now.json?key=%s&location=%s&language=zh-Hans&unit=c' % (self.private_key, self.location)
        r = requests.get(url)
        result = json.loads(r.text)
        now = result['results'][0]['now']
        return (now['text'], now['temperature'])

    def daily(self):
        url = 'https://api.seniverse.com/v3/weather/daily.json?key=%s&location=%s&language=zh-Hans&unit=c&start=0&days=5' % (self.private_key, self.location)
        r = requests.get(url)
        result = json.loads(r.text)
        daily = result['results'][0]['daily']
        infos = self.parse(daily)
        return infos

    def parse(self, daily):
        contents = []
        for info in daily:
            content = (info['text_day'], info['text_night'], info['low'], info['high'])
            contents.append(content)

        return contents


if __name__ == '__main__':
    w = Weather()

    now = w.now()
    now_text = '当前天气为 %s, 温度为 %s' % (now[0], now[1])

    daily = w.daily()
    today = daily[0]
    tomorrow = daily[1]
    after_tomorrow = daily[2]
    today_text = '今天白天 %s， 今天夜间 %s， 最高气温 %s， 最低气温%s' % (today[0], today[1], today[2], today[3])
    tomorrow_text = '明天白天 %s， 明天夜间 %s， 最高气温 %s， 最低气温%s' % (tomorrow[0], tomorrow[1], tomorrow[2], tomorrow[3])
    after_tomorrow_text = '后天白天 %s， 明天夜间 %s， 最高气温 %s， 最低气温%s' % (after_tomorrow[0], after_tomorrow[1], after_tomorrow[2], after_tomorrow[3])

    greeting_text = '乖乖懒提醒您'
    daily_text = greeting_text + '\n\n' + now_text + '\n\n' + today_text + '\n\n' + tomorrow_text + '\n\n' + after_tomorrow_text

    robot = DingRobot(DingRobot.XIN_ZHI_WEATHER)
    robot.send_text(now_text)
    robot.send_text(daily_text)
