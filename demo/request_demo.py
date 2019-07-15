# -*- coding: utf-8 -*-

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_proxies():
    url = 'http://47.103.22.188:5010/get/'
    response = requests.get(url)
    ip = response.text
    return {'http': 'http://' + ip, 'https': 'https://' + ip}


def selenium_request(url):
    # user agent
    dcap = DesiredCapabilities.PHANTOMJS
    dcap['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'

    # proxy
    ip = get_proxies()['http'].split('http://')[1]
    proxy_args = ['--proxy=%s' % ip, '--proxy-type=http', '--ignore-ssl-errors=true']
    service_args = proxy_args

    # driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.implicitly_wait(10)
    # print(driver.execute_script('return navigator.userAgent'))
    print('********request begin********')
    print('url = %s' % url)
    driver.get(url)
    result = driver.page_source

    print(result)
    with open('selenuim_source.txt', 'w') as file:
        file.write(result)
        file.close()
    return result


# url = 'https://www.feixiaohao.com/currencies/vollar/'
# selenium_request(url)

url = 'https://www.feixiaohao.com/currencies/vollar/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
r = requests.get(url, headers=headers, timeout=5)

html = etree.HTML(r.text)
price = html.xpath('//span[@class="val textGreen"]/span/text()')
print(price)

with open('content.txt', 'w') as file:
    file.write(r.text)
    file.close()
