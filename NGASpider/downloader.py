# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from lxml import etree
import json
import random
import requests


class Downloader(object):
    MAX_REPEAT_COUNT = 10
    USER_AGENT_KEY = 'phantomjs.page.settings.userAgent'
    USER_AGENT_VALUE = 'Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    SERVICE_ARGS = ['--load-images=no', '--disk-cache=yes', '--ignore-ssl-errors=true']

    def __init__(self):
        self.source = ''
        self.repeat_count = 0
        self.ip_random = -1

    def download(self, url):
        url = 'https://bbs.nga.cn/thread.php?fid=-7&page=1'
        cookies = 'taihe=7600c7a9985442930ed64f734be6deb2; UM_distinctid=16b64790f47a2-00ac2dedac08c7-123f6e57-1fa400-16b64790f48931; CNZZDATA1256638919=199523779-1560760185-https%253A%252F%252Fbbs.nga.cn%252F%7C1560760185; CNZZDATA30043604=cnzz_eid%3D32404797-1543800077-null%26ntime%3D1561010675; CNZZDATA30039253=cnzz_eid%3D1381056346-1543799614-null%26ntime%3D1561011686; CNZZDATA1256638820=553439814-1560757347-https%253A%252F%252Fbbs.nga.cn%252F%7C1561011366; ngacn0comUserInfo=%25C6%25AF%25C1%25C1%25C5%25F3%25D3%25D1%25A1%25A3%09%25E6%25BC%2582%25E4%25BA%25AE%25E6%259C%258B%25E5%258F%258B%25E3%2580%2582%0939%0939%09%0910%09200%094%090%090%0961_1; ngaPassportUid=42354193; ngaPassportUrlencodedUname=%25C6%25AF%25C1%25C1%25C5%25F3%25D3%25D1%25A1%25A3; ngaPassportCid=X8q9uoalva71m98lmg81v717khn1f8lugc7fi8m6; lastvisit=1561014777; lastpath=/read.php?tid=12531153; ngacn0comUserInfoCheck=360d760ceaf2b01621ac4ce696b8b829; ngacn0comInfoCheckTime=1561014777; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A1%2C1%3A1561370132%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-34%2C1%3A1561050096%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1561050096%7D%7D; Hm_lvt_5adc78329e14807f050ce131992ae69b=1560765254,1560765384,1561014782,1561015443; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1561015443; taihe_session=003b78bd1cf0a10ccc93c4c91f08f638'
        cookie = {}
        for line in cookies.split(';'):
            name, value = cookies.strip().split('=', 1)
            cookie[name] = value

        header = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        ip_random, proxies = self.get_proxies(-1)
        r = requests.get(url, cookies=cookie, headers=header, proxies=proxies, timeout=20)
        r.encoding = 'gbk'
        source = r.text

        # # user agent
        # dcap = DesiredCapabilities.PHANTOMJS
        # dcap['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
        # # dcap = dict(DesiredCapabilities.PHANTOMJS)
        # # dcap[self.USER_AGENT_KEY] = self.USER_AGENT_VALUE

        # # proxy
        # ip_rand, proxy = self.get_proxies(self.ip_random)
        # proxy_args = ['--proxy=%s' % proxy, '--proxy-type=http', '--ignore-ssl-errors=true']
        # service_args = proxy_args + self.SERVICE_ARGS
        # # service_args = self.SERVICE_ARGS

        # driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)
        # # driver = webdriver.PhantomJS(desired_capabilities=dcap)
        # driver.set_page_load_timeout(10)
        # driver.set_script_timeout(10)
        # driver.get(url)
        # source = driver.page_source
        # print(driver.execute_script('return navigator.userAgent'))

        # driver.get("about:black")

        # if self.repeat_count < 10:
            # url = self.check(source)
            # if url is not None:
                # source = self.download(url)
        # else:
            # print('download error')

        return source

    def check(self, source):
        while(True):
            sleep(1)

            html = etree.HTML(source)
            redirect_link = html.xpath('//a[text()="如不能自动跳转 可点此链接"]/@href')

            if len(redirect_link) > 0:
                url = 'https://bbs.nga.cn' + redirect_link[0]
                print('redirect to %s' % url)
                return url
            else:
                return None

            self.repeat_count += 1

    def get_proxies(self, random_number):
        with open('ip.txt', 'r',) as file:
            proxies = json.load(file)
            if random_number == -1:
                random_number = random.randint(0, len(proxies) - 1)
            proxy_info = proxies[random_number]
            ip = proxy_info['address']
            port = proxy_info['port']
            ip_url = '://' + ip + ':' + port
            proxy = {'http': 'http' + ip_url, 'https': 'https' + ip_url}
            print('random_number = %d, proxy = %s' % (random_number, proxy))
            return random_number, proxy


if __name__ == '__main__':
    # downloader = Downloader()
    # random, proxy = downloader.get_proxies(-1)
    # proxy_args = ['--proxy=%s' % proxy, '--proxy-type=http', '--ignore-ssl-errors=true']
    # print(proxy_args)

    # url = 'https://bbs.nga.cn/thread.php?fid=-7&page=1'
    # # url = 'http://www.baidu.com'
    # downloader = Downloader()
    # source = downloader.download(url)
    # print(source)


    url = 'https://bbs.nga.cn/thread.php?fid=-7&page=1'
    # url = 'http://www.baidu.com'
    downloader = Downloader()
    source = downloader.download(url)
    print(source)
    # random, proxy = downloader.get_proxies(-1)
    # headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
    # proxies = {'https': proxy}
    # r = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    # r.encoding = 'GB18030'
    # r.encoding = 'utf-8'
    # print(r.text)
