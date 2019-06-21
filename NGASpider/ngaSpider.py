# -*- coding: utf-8 -*-

from lxml import etree
from downloader import Downloader
from parse import Parse
from DB import DB
from time import sleep


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
    source = ngaDownloader.download(url)
    # source = openFile()

    html = etree.HTML(source)
    topics = html.xpath("//tbody[//a[@class='topic']][//a[@class='author']][//span[@class='replyer']]")
    for topic in topics:
        title = topic.xpath("//a[@class='topic']/text()")
        reply_count = topic.xpath("//a[@class='replies']/text()")
        author = topic.xpath("//a[@class='author']/text()")
        author_id = topic.xpath("//a[@class='author']/@title")
        create_time = topic.xpath("//a[@class='author']/following::span[1]/text()")
        replyer = topic.xpath("//span[@class='replyer']/text()")

    html = etree.HTML(source)
    html_str = etree.tostring(html, encoding='utf-8').decode('utf-8')
    writeToFile(html_str)

    db = DB()
    db.connect()

    for i in range(len(topics)):
        topic = (title[i], author[i], author_id[i], replyer[i], reply_count[i], create_time[i])
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
