# -*- coding: utf-8 -*-

from lxml import etree


class Localization(object):

    def parse(self):
        with open('./WorkboxiOS/Localization.plist', 'rb') as file:
            xml = file.read()
            html = etree.XML(xml)
            keys = html.xpath("//key")

            result = {}
            for element in keys:
                key = element.text
                # values = element.xpath(".././array[1]/string/text()")
                values = element.xpath("following::array[1]/string/text()")
                result[key] = values

            return result

    def generateSwift(self, d):
        swift = ''

        header = self.generate_header()
        import_str = self.generate_import()
        localization_begin = 'enum Localization {'
        localization_end = '}'
        tab = '    '

        # 添加头部信息
        swift += header

        # 添加import信息
        swift += '\n\n' + import_str

        # 创建枚举
        swift += '\n\n' + localization_begin
        for key in d:
            key_begin = tab + 'enum %s {' % key
            key_end = tab + '}'
            # 创建子枚举
            swift += '\n' + key_begin

            values = d[key]
            for value in values:
                value_str = tab + tab + 'static let %s = NSLocalizedString("%s.%s", comment: "%s.%s")' % (value, key, value, key, value)
                # 写static变量用于调用
                swift += '\n' + value_str

            # 子枚举结束
            swift += '\n' + key_end

        # 枚举结束
        swift += '\n' + localization_end
        print(swift)

        self.write(swift)

    def generate_header(self):
        return '''\
//
//  Localization.swift
//  WorkboxiOS
//
//  Created by Liam on 2019/6/21.
//  Copyright © 2019 Naver Corp. All rights reserved.
// '''

    def generate_import(self):
        return 'import Foundation'

    def write(self, str):
        with open('./WorkboxiOS/Support/Localization.swift', 'w') as file:
            file.write(str)


if __name__ == '__main__':
    localization = Localization()
    result = localization.parse()
    localization.generateSwift(result)
