# -*- coding: utf-8 -*-

import requests
import json
from daily_weather_model import DailyWeatherModel


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
        models = self.parse(daily)
        return models

    def parse(self, daily):
        models = []
        for info in daily:
            model = DailyWeatherModel()
            model.day_code = info['code_day']
            model.day_text = info['text_day']
            model.night_code = info['code_night']
            model.night_text = info['text_night']
            model.temp_high = info['high']
            model.temp_low = info['low']
            models.append(model)

        return models
