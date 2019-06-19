# -*- coding: utf-8 -*-

from lxml import etree


class Parse(object):
    def __init__(self, source):
        self.html = etree.HTML(source)
        self.table = self.html.xpath("//table[@id='topicrows']")[0]

    def parse_create_time(self):
        results = self.table.xpath("//span[contains(@id,'t_pt')]/text()")
        return results

    def parse_reply_time(self):
        results = self.table.xpath("//a[contains(@id,'t_rt')]/text()")
        return results

    def parse_url(self):
        results = self.table.xpath("//a[contains(@id,'t_tt')]/@href")
        return results

    def parse_title(self):
        results = self.table.xpath("//a[contains(@id,'t_tt')]")
        titles1 = list(map(lambda x: x.xpath("text()"), results))
        titles = list()
        for i in range(len(titles1)):
            titles += titles1[i]

        for i in range(len(titles)):
            titles = list(map(lambda x: x.strip(), titles))
        titles = list(filter(None, titles))
        return titles

    def parse_reply(self):
        replies = list()
        reply_tag = self.table.xpath("//a[@class='replies']")
        for i in range(len(reply_tag)):
            if reply_tag[i].text is None:
                replies.append("")
            else:
                replies.append(reply_tag[i].text)

        return replies
