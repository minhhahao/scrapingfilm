# -*- coding: utf-8 -*-
from crawler.utils.moduleimport import *


class WebSpider(CrawlSpider):
    name = "film"

    def __init__(self, config_file=None, *args, **kwargs):
        super(WebSpider, self).__init__(*args, **kwargs)
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=log.ERROR).start()

        if config_file is not None:
            self.data_config = json.load(open(config_file))
        self.start_urls = self.data_config['start_urls']
        self.base_url = self.data_config['base_url']

        if self.data_config['rules']:
            # Get object rules from config file
            WebSpider.rules = [eval(rule)
                               for rule in self.data_config['rules']]
            # Recompile the Rules
            super(WebSpider, self)._compile_rules()

    def parse_product(self, response):
        if self.data_config is not None:
            print response.url

            item = CrawlerItem()
            fields_config = self.data_config['fields']
            for key, value in fields_config.iteritems():
                try:
                    xpath_config = value.get('xpath')
                    re_config = value.get('re')
                    python_config = value.get('python')
                    operator_config = value.get('operator')
                    if xpath_config is None and re_config is None and python_config is None and operator_config is None:
                        item[key] = value
                    else:
                        item[key] = WebSpider.extract_data(
                            self, response, key, xpath_config, re_config, python_config, operator_config)
                except AttributeError:
                    item[key] = value

            item['product_url'] = response.url
            try:
                item['product_name'] = fields_config['product_name']
            except Exception as e:
                print e
                print "Missing field 'product_name' on config input file! Please Check!"
            yield item

    # Extract data
    @staticmethod
    def extract_data(self, response, key, xpath_config, re_config, python_config, operator_config):
        data = None
        if isinstance(xpath_config, unicode):
            try:
                # xpath_config = xpath_config.encode('utf-8', 'ignore')
                xpath_config = u"%s" % xpath_config
                if re_config:
                    data = response.xpath(xpath_config).re(re_config)
                else:
                    data = response.xpath(xpath_config).extract()
            except Exception as e:
                print e

        elif isinstance(xpath_config, list):
            data = []
            try:
                if isinstance(operator_config, unicode):
                    operator_config = operator_config.encode('utf-8', 'ignore')
                    if "or" in operator_config:
                        for xpath_c in xpath_config:
                            if re_config:
                                xpath_c = u"%s" % xpath_c
                                ele = response.xpath(xpath_c).re(re_config)
                                if isinstance(ele, str):
                                    data.append(ele)
                                    break
                                elif isinstance(ele, list):
                                    data += ele
                                    break
                            else:
                                xpath_c = u"%s" % xpath_c
                                ele = response.xpath(xpath_c).extract()
                                data += ele
                                break

                    elif "and" in operator_config:
                        for xpath_c in xpath_config:
                            if re_config:
                                xpath_c = u"%s" % xpath_c
                                ele = response.xpath(xpath_c).re(re_config)
                                if isinstance(ele, str):
                                    data.append(ele)
                                elif isinstance(ele, list):
                                    data += ele
                            else:
                                xpath_c = u"%s" % xpath_c
                                ele = response.xpath(xpath_c).extract()
                                data += ele
            except Exception as e:
                print e

        if isinstance(python_config, unicode):
            try:
                data = eval(python_config.encode('utf-8', 'ignore'))
            except Exception as e:
                print e

        if key == 'description':
            return FormatData.description(self=self, input_value=data)
        if 'name' in key:
            return FormatData.name(self=self, input_value=data)
        elif key == 'image_poster':
            return FormatData.image_urls(self=self, input_value=data)
        elif key == 'country':
            return FormatData.country(self=self, input_value=data)
        elif key == 'film_status':
            return FormatData.film_status(self=self, input_value=data)
        elif key == 'film_type':
            return FormatData.film_type(self=self, input_value=data)
        elif key == 'ishd':
            return FormatData.ishd(self=self, input_value=data)
        elif key == 'sub':
            return FormatData.sub(self=self, input_value=data)
        elif key == 'year':
            return FormatData.year(self=self, input_value=data)
        else:
            return FormatData.other(self=self, input_value=data)
