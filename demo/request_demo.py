# -*- coding: utf-8 -*-

import requests
from lxml import etree


def get_proxies(self):
    url = 'http://47.103.22.188:5010/get/'
    response = requests.get(url)
    ip = response.text
    return {'http': 'http://' + ip, 'https': 'https://' + ip}


url = 'https://www.feixiaohao.com/currencies/vollar/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
r = requests.get(url, headers=headers, timeout=5)

html = etree.HTML(r.text)
price = html.xpath('//span[@class="val textGreen"]/span/text()')
print(price)

with open('content.txt', 'w') as file:
    file.write(r.text)
    file.close()
