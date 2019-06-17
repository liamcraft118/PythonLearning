# -*- coding: utf-8 -*-

import requests
import json

open_id = 'gh_b476741b6c87'
template_id = 'Iv0HXcd-Q9j3J1FEPn0LHcQAFZYK6uYOw58thnuCOmg'

appid = 'wx611d4e44cd402aab'
appsecret = 'a4a2d0f5df6ee73391e01a24cbcdb39c'

url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid, appsecret)
response = requests.get(url)
json_data = response.text
data = json.loads(json_data)
access_token = data['access_token']

msg = {
    'touser': 'oPoDY1I02r_PahhTg6zvWQ3QgRy0',
    'template_id': template_id,
    'data': {
        'content': {
            'value': '每日一句天天向上',
            'color': '#0000CD'
        }
    }
}

json_data = json.dumps(msg)
url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % str(access_token)
response = requests.post(url, data=json_data)
result = response.text
print(json.loads(result))

