# -*- coding: utf-8 -*-

import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Downloader:
    def __init__(self):
        self.proxies = self.get_proxies()
        self.timeout = 3
        requests.session().keep_alive = False

    def request(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        print('********request begin********')
        print('url = %s' % url)
        print('proxies = %s' % self.proxies)
        try:
            r = requests.get(url, headers=headers, proxies=self.proxies, timeout=self.timeout)
        except requests.exceptions.RequestException as e:
            self.proxies = self.get_proxies()
            result = None
            print('!!!!!!!!!!!!!!!!!')
            print(e)
            print('!!!!!!!!!!!!!!!!!')
        # except OSError:
            # result = None
            # print('!!!!!!!!!OS ERROR!!!!!!!!')
        else:
            result = r.text
            print('********request end********')
        return result

    def selenium_request(self, url):
        # user agent
        dcap = DesiredCapabilities.PHANTOMJS
        dcap['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'

        # proxy
        ip = self.get_proxies()['http'].split('http://')[1]
        proxy_args = ['--proxy=%s' % ip, '--proxy-type=http', '--ignore-ssl-errors=true']
        service_args = proxy_args

        driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)
        # driver = webdriver.PhantomJS(desired_capabilities=dcap)
        driver.set_page_load_timeout(5)
        driver.set_script_timeout(5)
        # print(driver.execute_script('return navigator.userAgent'))
        print('********request begin********')
        print('url = %s' % url)
        print('proxies = %s' % self.proxies)
        try:
            driver.get(url)
        except:
            self.proxies = self.get_proxies()
            result = None
            print('!!!!!!!!!!!!!!!!!ERROR!!!!!!!!!!!!!!!')
            # print('!!!!!!!!!!!!!!!!!')
            # print(e)
            # print('!!!!!!!!!!!!!!!!!')
        else:
            result = driver.page_source
            if len(result) < 1000:
                result = None

        if result is None:
            self.proxies = self.get_proxies()

        print(result)
        # with open('selenuim_source.txt', 'w') as file:
            # file.write(result)
            # file.close()
        return result

    def get_proxies(self):
        url = 'http://47.103.22.188:5010/get/'
        response = requests.get(url)
        ip = response.text
        return {'http': 'http://' + ip, 'https': 'https://' + ip}


if __name__ == '__main__':
    url = 'https://2.taobao.com/item.htm?id=598183962091'
    # url = 'https://2.taobao.com/item.htm?spm=2007.1000337.18.2.218a6818WqwUcw&id=598093685695'

    downloader = Downloader()
    downloader.selenium_request(url)
