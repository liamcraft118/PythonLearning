# -*- coding: utf-8 -*-

from wxpy import *

bot = Bot()
print('!!!!!')
my_friend = bot.friends().search('漂亮朋友')[0]
print('*******')
my_friend.send('Hello WeChat!')
