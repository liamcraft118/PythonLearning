# -*- coding: utf-8 -*-

from lxml import etree
from downloader import Downloader
from parse import Parse
from DB import DB


class Topic:
    def __init__(self):
        self.theme = ''
        self.title = ''
        self.url = ''
        self.reply = ''
        self.create_time = ''
        self.reply_time = ''


def openFile():
    with open('nga.txt', 'r', encoding='utf-8') as f:
        source = f.read()
        f.close()
        return source


def writeToFile(html_str):
    with open('nga.txt', 'w', encoding='utf-8') as f:
        f.write(html_str)
        f.close


def downloadPage(ngaDownloader, index):
    url = 'https://bbs.nga.cn/thread.php?fid=-7&page=%d' % index
    # source = ngaDownloader.download(url)
    source = openFile()

    html = etree.HTML(source)
    # content = html.xpath("//tbody//a[@class='topic']/text() \
                         # | //tbody//a[@class='author']/text() \
                         # | //tbody//a[@class='author']/@title \
                         # | //tbody//span[contains(@id,'t_pt')]/text() \
                         # | //tbody//span[contains(@id,'t_tr')]/text()")
    # tbody = html.xpath("//tbody")[0]
    # topic = tbody.xpath("a")
    topic = html.xpath("//tbody[//a[@class='topic']][//a[@class='author']][//span[@class='replyer']]")
    # content = tbody.xpath("//a[@class='topic']text()")
    print(topic)

    return
    html = etree.HTML(source)
    html_str = etree.tostring(html, encoding='utf-8').decode('utf-8')
    writeToFile(html_str)


    topics = list()
    parse = Parse(source)
    replies = parse.parse_reply()
    create_times = parse.parse_create_time()
    reply_times = parse.parse_reply_time()
    urls = parse.parse_url()
    titles = parse.parse_title()

    db = DB()
    db.connect()

    print('replies %s' % len(replies))
    print('create_times %s' % len(create_times))
    print('reply_times %s' % len(reply_times))
    print('urls %s' % len(urls))
    print('titles %s' % len(titles))
    for i in range(len(replies)):
        topic = Topic()
        topic.reply = replies[i]
        topic.create_time = create_times[i]
        # topic.reply_time = reply_times[i]
        topic.url = urls[i]
        topic.title = titles[i]
        topics.append(topic)
        print(vars(topic))

        # insert
        db.insert(topic)

    db.commit()


def main():
    ngaDownloader = Downloader()
    downloadPage(ngaDownloader, 1)

    # for i in range(1, 101):
        # ngaDownloader = Downloader()
        # downloadPage(ngaDownloader, i)


if __name__ == '__main__':
    main()
