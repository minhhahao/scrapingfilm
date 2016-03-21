from crawler.utils.moduleimport import *


class GlobalSpider(CrawlSpider):
    name = "t"
    start_urls = ["http://topthuthuat.com/"],
    # def __init__(self, config_file=None, *a, **kw):
    #     super(GlobalSpider, self).__init__(*a, **kw)
    #     if config_file is not None:
    #         self.MY_CONFIG = json.load(open(config_file))
    #
    #     self.start_urls = self.MY_CONFIG['start_urls']
    #     self.fields = self.MY_CONFIG['fields']
    # if self.MY_CONFIG['rules']:
    #     GlobalSpider.rules = [i for i in self.MY_CONFIG['rules']]

    rules = [
        Rule(lxml(allow=('.*',), restrict_xpaths=("//div[@class='pagination-bg']/a")), follow=True),
        Rule(lxml(allow=('.*',), restrict_xpaths=("//h1[@class='pos-title']/a")), callback='parse_product')
    ]

    def parse_product(self, response):
        import pdb
        pdb.set_trace()
        self.log("Crawling: %s" % response.url, level=log.INFO)

        hxs = HtmlXPathSelector(response)
        item = CrawlerItem()

        data_config = self.fields
        for key in data_config.keys():
            try:
                # hard code
                if isinstance(data_config.get(key), unicode):
                    item[key] = data_config.get(key).encode('utf-8', 'ignore')
                else:
                    xpath_config = data_config.get(key).get('xpath')
                    value_xpath = []

                    python_config = data_config.get(key).get('python')
                    re_config = data_config.get(key).get('re')
                    data_type = data_config.get(key).get('type')

                    # xpath
                    if isinstance(xpath_config, unicode):
                        value_xpath = hxs.xpath(xpath_config.encode('utf-8', 'ignore'))
                    elif isinstance(xpath_config, list):
                        for x in xpath_config:
                            element = hxs.xpath(x)
                            value_xpath += element

                    # regex
                    if isinstance(re_config, unicode):
                        data = [re.findall(re_config.encode('utf-8', 'ignore'), value) for value in value_xpath]
                    else:
                        data = [value.extract() for value in value_xpath]

                    # python
                    if isinstance(python_config, unicode):
                        data = [eval(python_config.encode('utf-8', 'ignore'))]

                    # type content
                    if isinstance(data_type, unicode):
                        if 'list' in data_type.encode('utf-8', 'ignore'):
                            item[key] = data
                        elif 'number' in data_type.encode('utf-8', 'ignore'):
                            item[key] = float(''.join(data))
                    else:
                        item[key] = ''.join(data)

            except Exception as e:
                print e
        yield item
