# -*- coding: utf-8 -*-

import json

text = '{"status": "success", "data": {"feedback": "", "logo": false, "s": "2d577237", "i18n_labels": {"next": "\u6b63\u5728\u52a0\u8f7d\u9a8c\u8bc1", "next_ready": "\u8bf7\u5b8c\u6210\u9a8c\u8bc1", "refresh_page": "\u9875\u9762\u51fa\u73b0\u9519\u8bef\u5566\uff01\u8981\u7ee7\u7eed\u64cd\u4f5c\uff0c\u8bf7\u5237\u65b0\u6b64\u9875\u9762", "success_title": "\u901a\u8fc7\u9a8c\u8bc1", "error_content": "\u8bf7\u70b9\u51fb\u6b64\u5904\u91cd\u8bd5", "ready": "\u70b9\u51fb\u6309\u94ae\u8fdb\u884c\u9a8c\u8bc1", "error": "\u7f51\u7edc\u4e0d\u7ed9\u529b", "loading_content": "\u667a\u80fd\u9a8c\u8bc1\u68c0\u6d4b\u4e2d", "reset": "\u8bf7\u70b9\u51fb\u91cd\u8bd5", "fullpage": "\u667a\u80fd\u68c0\u6d4b\u4e2d", "error_title": "\u7f51\u7edc\u8d85\u65f6", "success": "\u9a8c\u8bc1\u6210\u529f", "goto_cancel": "\u53d6\u6d88", "goto_confirm": "\u524d\u5f80", "copyright": "\u7531\u6781\u9a8c\u63d0\u4f9b\u6280\u672f\u652f\u6301", "goto_homepage": "\u662f\u5426\u524d\u5f80\u9a8c\u8bc1\u670d\u52a1Geetest\u5b98\u7f51"}, "c": [12, 58, 98, 36, 43, 95, 62, 15, 12], "theme": "wind", "theme_version": "1.5.5", "static_servers": ["static.geetest.com", "dn-staticdown.qbox.me"], "api_server": "api.geetest.com"}}'
r = json.loads(text)
print(r)
