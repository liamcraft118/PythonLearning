# -*- coding: utf-8 -*-

import requests


class DingRobot:

    XIN_ZHI_WEATHER = '7b6a1bdecfb7b2e9a4a106d6953622214d9c8e7d1f833e6ed02ca65749cd0221'

    def __init__(self, robot_token):
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % robot_token
        self.headers = {'Content-Type': 'application/json'}
        self.data = {'msgtype': 'text', 'text': {'content': ''}}

    def send_text(self, text):
        self.data['text']['content'] = text
        try:
            requests.post(self.url, headers=self.headers, json=self.data, timeout=3)
        except requests.exceptions.RequestException as e:
            print(e)
# url = 'https://oapi.dingtalk.com/robot/send?access_token=7b6a1bdecfb7b2e9a4a106d6953622214d9c8e7d1f833e6ed02ca65749cd0221'


if __name__ == '__main__':
    robot = DingRobot(DingRobot.XIN_ZHI_WEATHER)
    robot.send_text('hello')
