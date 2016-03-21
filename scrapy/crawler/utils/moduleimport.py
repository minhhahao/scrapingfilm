from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.log import ScrapyFileLogObserver
from scrapy import log
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.selector.unified import SelectorList
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor as lxml
# import lxml
from lxml.html.clean import clean_html
import lxml.html.clean as clean

from scrapy import FormRequest
from scrapy import Request
from scrapy import log

from urlparse import urljoin

from crawler.items import *
from crawler.utils.formatdata import *
from crawler.utils.html_string import *

import os
import json
import re
import unicodedata
import locale
import traceback

from crawler.supportclient.hdviet import *
from crawler.supportclient.khothuthuat import *
from crawler.supportclient.xemphimso import *





