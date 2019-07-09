# -*- coding: utf-8 -*-

import requests

r = requests.get('http://172.17.29.151:5010/get')
# r = requests.get('http://47.103.22.188:5010/get')
print(r.text)
