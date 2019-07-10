# -*- coding: utf-8 -*-

from downloader import Downloader
import analyzer
import fileManager


class XianYuCrawler:
    def __init__(self):
        self.page = 0
        self.downloader = Downloader()
        self.file_name = 'content.txt'
        self.detail_file_name = 'detail.txt'

    def run(self):
        key = 'apple pencil'
        print('key = %s' % (key))
        while True:
            # text = fileManager.read(self.file_name)

            url = 'https://s.2.taobao.com/list/?q=%s&page=%s&search_type=item&_input_charset=utf8' % (key, self.page)
            text = self.request(url)
            fileManager.write(self.file_name, text)

            list_info = analyzer.analyze_xianyu_list(text)
            detail_url_list = list_info[0]
            for detail_url in detail_url_list:
                url = 'https:' + detail_url
                text = self.request(url)
                # text = self.selenium_request(url)
                fileManager.write(self.detail_file_name, text)

            self.page += 1
            print('@@@@@@@@@@@page %s finish@@@@@@@@@@@' % self.page)

    def request(self, url):
        text = self.downloader.request(url)
        if text is None:
            return self.request(url)
        return text

    def selenium_request(self, url):
        text = self.downloader.selenium_request(url)
        if text is None:
            return self.selenium_request(url)
        return text


if __name__ == '__main__':
    crawler = XianYuCrawler()
    crawler.run()
