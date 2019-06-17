# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree

url = 'https://bbs.nga.cn/thread.php?fid=-7'

# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
# driver = webdriver.PhantomJS(desired_capabilities=dcap)
# driver.get(url)
# source = driver.page_source
# driver.close()

source = ""
with open('nga.txt', 'r', encoding='utf-8') as f:
    source = f.read()
    f.close()

# print(source)

def textable(element):
    return element.text

html = etree.HTML(source)
# result = html.xpath("//table[@id='topicrows']//span[@class='silver']")
result = html.xpath("//table[@id='topicrows']//a[text() and @id='t_tt1_0']")
# result = list(map(textable, result))
# print(type(result[0]))
print(result[0])
