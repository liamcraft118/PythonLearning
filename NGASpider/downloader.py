# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from lxml import etree


class Downloader(object):
    MAX_REPEAT_COUNT = 10

    def __init__(self):
        self.source = ''
        self.repeat_count = 0


    def download(self, url):
        service_args = []
        service_args.append('--load-images=no')
        service_args.append('--disk-cache=yes')
        service_args.append('--ignore-ssl-errors=true')
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        userAgent = 'phantomjs.page.settings.userAgent'
        userAgentValue = '''Mozilla/5.0 (Macintosh; Intel Mac OS X)
        AppleWebKit/538.1 (KHTML, like Gecko)
        Chrome/62.0.3202.94 Safari/537.36'''
        dcap[userAgent] = userAgentValue
        driver = webdriver.PhantomJS(desired_capabilities=dcap,
                                          service_args=service_args)
        driver.get(url)
        source = driver.page_source

        driver.get("about:black")

        if self.repeat_count < 10:
            url = self.check(source)
            if url is not None:
                source = self.download(url)
        else:
            print('download error')

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
