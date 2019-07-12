# -*- coding: utf-8 -*-

from weather import Weather
import time
from ding_robot import DingRobot
from weather_db import weather_db


if __name__ == '__main__':
    w = Weather()

    # now
    now = w.now()
    now_text = '当前天气为 %s, 温度为 %s' % (now[0], now[1])

    # daily
    daily = w.daily()
    today = daily[0]
    tomorrow = daily[1]
    after_tomorrow = daily[2]
    today_text = '今天白天 %s, 今天夜间 %s,\n 最高气温 %s, 最低气温%s' % (today.day_text, today.night_text, today.temp_high, today.temp_low)
    tomorrow_text = '明天白天 %s, 明天夜间 %s,\n 最高气温 %s, 最低气温%s' % (tomorrow.day_text, tomorrow.night_text, tomorrow.temp_high, tomorrow.temp_low)
    after_tomorrow_text = '后天白天 %s, 明天夜间 %s,\n 最高气温 %s, 最低气温%s' % (after_tomorrow.day_text, after_tomorrow.night_text, after_tomorrow.temp_high, after_tomorrow.temp_low)

    # greeting
    weeks = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
    localtime = time.localtime()
    week_code = int(time.strftime("%w", localtime))
    week_text = weeks[week_code]
    date_text = time.strftime("%Y年%m月%d日", time.localtime())
    time_text = '今天是' + ' ' + date_text + ' ' + week_text
    greeting_text = '乖乖懒提醒您'
    daily_text = time_text + '\n\n' + greeting_text + '\n\n' + now_text + '\n\n' + today_text + '\n\n' + tomorrow_text + '\n\n' + after_tomorrow_text

    # db
    db = weather_db()
    db.connect()

    yesterday_night_code = int(db.fetch_latest_weather()[4])

    today.date_formatted = date_text
    info = (today.date_formatted, today.day_code, today.day_text, today.night_code, today.night_text, today.temp_high, today.temp_low)
    db.insert_daily_weather(info)

    db.commit()
    db.close()

    today_day_code = int(today.day_code)
    get_better = yesterday_night_code > 9 and today_day_code <= 9
    get_worse = yesterday_night_code <= 9 and today_day_code > 9

    # robot
    robot = DingRobot(DingRobot.XIN_ZHI_WEATHER)
    if get_better:
        robot.send_text('今天应该不下雨了\n\n' + daily_text)
    elif get_worse:
        robot.send_text('今天可能会下雨,记得带伞哦\n\n' + daily_text)
