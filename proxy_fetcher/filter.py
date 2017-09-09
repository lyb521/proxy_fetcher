# coding=utf-8
import urllib
import time

urllib.socket.setdefaulttimeout(5)


class IPChecker(object):
    url = 'http://ip138.com'

    def check(self, item):
        start_time = time.time()
        try:
            proxies = {
                item['protocol']: 'http://%s:%s' % (item['ip'], item['port']),
            }
            request = urllib.urlopen(self.url, proxies=proxies)
            content = request.read()
        except:
            return False
        end_time = time.time()
        item['verify_time'] = int(start_time)
        item['delay'] = round(end_time - start_time, 4)
        # KB/s
        item['speed'] = round(len(content) * 1.0 / 1024 / item['delay'], 2)
        return item
