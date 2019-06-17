# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = 'https://bbs.nga.cn/thread.php?fid=-7'

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.get(url)
source = driver.page_source
print(source)
driver.close()
