from scrapy import log
import re


class RandomProxy(object):
    def __init__(self, settings):
        self.proxy_list = settings.get('PROXY_LIST')
        self.proxies = {}
        with open(self.proxy_list) as proxy:
            lines = proxy.readlines()

            for line in lines:
                line = "http://%s" % line.strip("\n")
                parts = re.match('(\w+://)(\w+:\w+@)?(.+)', line)
                # Cut trailing @
                if parts.group(2):
                    user_pass = parts.group(2)[:-1]
                else:
                    user_pass = ''

                self.proxies[parts.group(1) + parts.group(3)] = user_pass

            proxy.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        url = spider.config
        if len(spider.config.proxy) > 0:
            proxy_address = "http://%s" % spider.config.proxy.encode("ascii", "ignore")
            request.meta['proxy'] = proxy_address
        # Don't overwrite with a random one (server-side state for IP)
        if 'proxy' in request.meta:
            return

    def process_exception(self, request, exception, spider):
        proxy = request.meta['proxy']
        log.msg('Removing failed proxy <%s>, %d proxies left' % (
            proxy, len(self.proxies)))
        try:
            del self.proxies[proxy]
        except ValueError:
            pass
