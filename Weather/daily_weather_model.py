# -*- coding: utf-8 -*-


class DailyWeatherModel(object):
    __slots__ = ('date_formatted', 'day_code', 'day_text', 'night_code', 'night_text', 'temp_high', 'temp_low')

    def __init__(self):
        self.date_formatted = None
        self.day_code = None
        self.day_text = None
        self.night_code = None
        self.night_text = None
        self.temp_high = None
        self.temp_low = None
