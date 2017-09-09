# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/3/13
# @Time: 19:44
# @Description:
import httplib
import json
import os
import random

import MySQLdb.cursors
import time
from config import *
import urllib
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf8')
proxy_item = {}
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# 手机浏览器
user_agent_list_mobile = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
]

def connect():
    return MySQLdb.connect(
        user=configs['db']['user'],
        passwd=configs['db']['passwd'],
        host=configs['db']['host'],
        db=configs['db']['database'],
        charset=configs['db']['charset']
    )


def _get_data(url):
    print url
    if proxy_item:
        proxys = proxy_item[random.randint(0, len(proxy_item))]
        # proxy = urllib2.ProxyHandler({proxys['protocol']: "%s:%s" % (proxys['ip'], proxys['port'])})
        proxy = urllib2.ProxyHandler({'http': '61.191.173.31:808'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        random_header = random.choice(user_agent_list)
        req_header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age = 0',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Connection': 'keep-alive',
            'Host': 'www.xicidaili.com',
            # 'Referer': url,  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
            "X-Forwarded-For": '',
            "If-None-Match": 'W/"4b3d5c6ab9a81b5bc28272f4cdadbefd"',
        }
        req = urllib2.Request(url, None, req_header)
        res = urllib2.urlopen(req, timeout=10).read()
        # print res
        return res
    try:
        if proxy_item :
            proxys = proxy_item[random.randint(0, len(proxy_item))]
            # proxy = urllib2.ProxyHandler({proxys['protocol']: "%s:%s" % (proxys['ip'], proxys['port'])})
            proxy = urllib2.ProxyHandler({'http': '119.5.1.14:808'})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)
            random_header = random.choice(user_agent_list)
            req_header = {
                'User-Agent': random_header,
                'Accept':  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Cache-Control': 'max-age = 0',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'Connection': 'keep-alive',
                'Host': 'www.xicidaili.com',
                'Referer': url,  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
                "X-Forwarded-For": proxys['ip'],
                }
            req = urllib2.Request(url, None, req_header)
            res = urllib2.urlopen(req, timeout=10).read()
            # print res
            return res
        else:
            return False
    except httplib.IncompleteRead, e:
        return False
    except urllib2.HTTPError, e:
        return False
    except urllib2.URLError, e:
        return False
    except Exception as err:
        return False

# 获取代理
def _get_proxy():
    return urllib2.urlopen('http://api.leiyongbo.com/proxy.php', timeout=5).read()


def is_json(myjson):
    try:
        json.loads(myjson)
    except Exception:
        return False
    return True

if __name__ == '__main__':
    proxy_item = json.loads(_get_proxy())['data']
    ret = _get_data('http://www.xicidaili.com')
    print ret
