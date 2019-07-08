# -*- coding: utf-8 -*-

from lxml import etree
from downloader import Downloader


class XianYuCrawler:
    def __init__(self):
        self.page = 0
        self.downloader = Downloader()

    def run(self):
        key = 'apple pencil'
        print('key = %s' % (key))
        while True:
            url = 'https://s.2.taobao.com/list/?q=%s&page=%s&search_type=item&_input_charset=utf8' % (key, self.page)
            text = self.downloader.request(url)
            # text = self.read_file()
            if text is None:
                continue
            self.analyze(text)
            self.page += 1
            self.write_to_file(text)
            print('success')

    def analyze(self, text):
        html = etree.HTML(text)
        item_pic_list = html.xpath('//div[@class="item-pic sh-pic120"]')
        item_new_list = []
        thumbnail_url_list = []
        print('item_pic_list %s' % len(item_pic_list))
        for item_pic in item_pic_list:
            thumbnail_url = (item_pic.xpath('a/img/@src') or [None])[0]
            item_new = (item_pic.xpath('span/text()') or [None])[0]
            thumbnail_url_list.append(thumbnail_url)
            item_new_list.append(item_new)

        detail_url_list = html.xpath('//h4[@class="item-title"]/a/@href')
        title_list = html.xpath('//h4[@class="item-title"]/a/text()')
        price_list = html.xpath('//span[@class="price"]/em/text()')
        description_list = html.xpath('//div[@class="item-description"]/text()')
        publish_time_list = html.xpath('//span[@class="item-pub-time"]/text()')
        comment_number_list = html.xpath('//div[@class="item-count"]/a/em/text()')
        print('detail_url_list %s' % len(detail_url_list))
        print('titles %s' % len(title_list))
        print('prices %s' % len(price_list))
        print('description_list %s' % len(description_list))
        print('publish_time_list %s' % len(publish_time_list))
        print('comment_number_list %s' % len(comment_number_list))

    def read_file(self):
        with open('content.txt', 'r') as file:
            text = file.read()
            file.close()
        return text

    def write_to_file(self, text):
        with open('content.txt', 'w') as file:
            file.write(text)
            file.close()


if __name__ == '__main__':
    crawler = XianYuCrawler()
    crawler.run()

