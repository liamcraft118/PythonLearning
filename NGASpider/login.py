# -*- coding: utf-8 -*-

import requests
from lxml import etree


# class NGALogin(object):


if __name__ == '__main__':
    url = 'https://bbs.nga.cn/thread.php?fid=-7&page=1'
    cookies = 'taihe=7600c7a9985442930ed64f734be6deb2; UM_distinctid=16b64790f47a2-00ac2dedac08c7-123f6e57-1fa400-16b64790f48931; CNZZDATA1256638919=199523779-1560760185-https%253A%252F%252Fbbs.nga.cn%252F%7C1560760185; CNZZDATA30043604=cnzz_eid%3D32404797-1543800077-null%26ntime%3D1561010675; CNZZDATA30039253=cnzz_eid%3D1381056346-1543799614-null%26ntime%3D1561011686; CNZZDATA1256638820=553439814-1560757347-https%253A%252F%252Fbbs.nga.cn%252F%7C1561011366; ngacn0comUserInfo=%25C6%25AF%25C1%25C1%25C5%25F3%25D3%25D1%25A1%25A3%09%25E6%25BC%2582%25E4%25BA%25AE%25E6%259C%258B%25E5%258F%258B%25E3%2580%2582%0939%0939%09%0910%09200%094%090%090%0961_1; ngaPassportUid=42354193; ngaPassportUrlencodedUname=%25C6%25AF%25C1%25C1%25C5%25F3%25D3%25D1%25A1%25A3; ngaPassportCid=X8q9uoalva71m98lmg81v717khn1f8lugc7fi8m6; lastvisit=1561014777; lastpath=/read.php?tid=12531153; ngacn0comUserInfoCheck=360d760ceaf2b01621ac4ce696b8b829; ngacn0comInfoCheckTime=1561014777; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A1%2C1%3A1561370132%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-34%2C1%3A1561050096%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1561050096%7D%7D; Hm_lvt_5adc78329e14807f050ce131992ae69b=1560765254,1560765384,1561014782,1561015443; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1561015443; taihe_session=003b78bd1cf0a10ccc93c4c91f08f638'
    cookie = {}
    for line in cookies.split(';'):
        name, value = cookies.strip().split('=', 1)
        cookie[name] = value
    print(cookie)
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    proxy = {'http': 'http://112.85.130.28:9999', 'https': 'https://112.85.130.28:9999'}
    r = requests.get(url, cookies=cookie, headers=header, proxies=proxy, timeout=5)
    r.encoding = 'gbk'
    print(r.text)

    # r = requests.get('https://bbs.nga.cn/thread.php?fid=-7&page=1')
    # r.encoding = 'gb18030'
    # print(r.text)
