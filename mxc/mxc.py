# -*- coding: utf-8 -*-

import requests


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
datas = {'password': '7957cf04024d0dd389b732026393d673',
         'account': 'ingocraft118@gmail.com',
         'geetest_offline': '1',
         'geetest_challenge': '3d4973f4519e2f2e5b7044e7b3dca7f0',
         'geetest_validate': 'b8504b7a8be64f57db73a4f0e1d26b8c',
         'geetest_seccode': 'b8504b7a8be64f57db73a4f0e1d26b8c|jordan'}
url = 'https://www.mxc.com/api/login'
r = requests.post(url, headers=headers, data=datas)
print(r.text)
