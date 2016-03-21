from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor as lxml
from scrapy.contrib.spiders import CrawlSpider, Rule


class TestRuleSpider(CrawlSpider):
    name = "rules"
    start_urls = ["http://phimnhanh.com/"]
    cpt = 0
    rules = [
        Rule(lxml(allow=('.*'), restrict_xpaths=("//div[@id='top-menu-ct']//a")), follow=True, ),
        Rule(lxml(allow=('.*'), restrict_xpaths=("//ul[@class='pagination']/li/a")), follow=True),
        Rule(lxml(allow=('.*'), restrict_xpaths=("//ul[@class='list_m']//h2/a")), callback='parse_product')
    ]

    def parse_product(self, response):
        self.cpt += 1
        print self.cpt
        print response.url
        # print self.cpt
        return None

    def passCat(self, response):
        print "passFollows------------------"
        self.cpt += 1
        print self.cpt
        print response.url
        return None
