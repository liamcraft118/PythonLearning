# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree

class Topic:
    # __slots__ = ('theme', 'title', 'url', 'reply', 'create_time', 'reply_time')
    def __init__(self):
        self.theme = ''
        self.title = ''
        self.url = ''
        self.reply = ''
        self.create_time = ''
        self.reply_time = ''

def vars2(x):
    if hasattr(x, '__dict__'):
        return vars(x)
    else:
        ret = {slot: getattr(x, slot) for slot in x.__slots__}
        for cls in type(x).mro():
            spr = super(cls, x)
            if not hasattr(spr, '__slots__'):
                break
            for slot in spr.__slots__:
                ret[slot] = getattr(x, slot)
        return ret

def download(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver.get(url)
    source = driver.page_source
    driver.close()

    return source

def openFile():
    with open('nga.txt', 'r', encoding='utf-8') as f:
        source = f.read()
        f.close()
        return source

def writeToFile(html_str):
    with open('nga.txt', 'w', encoding='utf-8') as f:
        f.write(html_str)
        f.close

def main():
    url = 'https://bbs.nga.cn/thread.php?fid=-7&rand=819'
    source = download(url)
    # source = openFile()


    while(True):
        html = etree.HTML(source)
        redirect_link = html.xpath('//a[text()="如不能自动跳转 可点此链接"]/@href')

        if len(redirect_link) > 0:
            url = 'https://bbs.nga.cn' + redirect_link[0]
            print('redirect to %s' % url)
            source = download(url)
        else:
            break


    html = etree.HTML(source)
    html_str = etree.tostring(html,encoding='utf-8').decode('utf-8')
    writeToFile(html_str)

    redirect_link = html.xpath('//a[text()="如不能自动跳转 可点此链接"]/@href')
    if len(redirect_link) > 0:
        print('error')
        return

    topics = []


    table = html.xpath("//table[@id='topicrows']")[0]
    result = table.xpath("//span[contains(@id,'t_pt')]/text() \
                        | //a[contains(@id,'t_rt')]/text() \
                        | //a[contains(@id,'t_tt')]/@href")
    # | //a[contains(@id,'t_tt')]/span/text() \
    step = 3
    create_times = result[::step]
    reply_times = result[1::step]
    urls = result[2::step]

    # a = table.xpath("//a[contains(@id,'t_tt')]")
    # for i in range(len(a)):
        # print(etree.tostring(a[i],encoding='utf-8').decode('utf-8'))
        # print(a[i].text)
        # print(a[i].xpath("text()"))
        # print()

    title_tag = table.xpath("//a[contains(@id,'t_tt')]")
    titles1 = list(map(lambda x: x.xpath("text()"), title_tag))
    titles = list()
    for i in range(len(titles1)):
        titles += titles1[i]

    for i in range(len(titles)):
        titles = list(map(lambda x: x.strip(), titles))
    titles = list(filter(None, titles))

    replies = list()
    reply_tag = table.xpath("//a[@class='replies']")
    # reply_tag = table.xpath("//span[contains(@id,'t_pt')]/text()")
    # reply_tag = table.xpath("//a[contains(@id,'t_rt')]/text()")
    # reply_tag = table.xpath("//a[contains(@id,'t_tt')]/@href")
    for i in range(len(reply_tag)):
        # print('!!!' + str(i))
        # print('!' + reply_tag[i].text)
        # print(reply_tag[i].text)
        # print(etree.tostring(reply_tag[i],encoding='utf-8').decode('utf-8'))
        # print(reply_tag[i].xpath("text()"))
        if reply_tag[i].text == None:
            replies.append("")
        else:
            replies.append(reply_tag[i].text)

    # url_tag = table.xpath("//a[contains(@id,'t_tt')]")
    # for i in range(len(url_tag)):
        # # print(i)
        # # print(url_tag[i])
        # print(etree.tostring(url_tag[i],encoding='utf-8').decode('utf-8'))

    for i in range(len(replies)):
        print(i)
        topic = Topic()
        topic.reply = replies[i]
        topic.create_time = create_times[i]
        topic.reply_time = reply_times[i]
        topic.url = urls[i]
        topic.title = titles[i]
        topics.append(topic)
        print(vars(topic))

    # dir(topics)


if __name__ == '__main__':
    main()
