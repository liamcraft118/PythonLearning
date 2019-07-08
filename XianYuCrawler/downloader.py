# -*- coding: utf-8 -*-

import requests


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

    def get_proxies(self):
        url = 'http://127.0.0.1:5010/get/'
        response = requests.get(url)
        ip = response.text
        return {'http': 'http://' + ip, 'https': 'https://' + ip}
