# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapy_balloons (+http://www.yourdomain.com)'
# COOKIES_DEBUG = True
ITEM_PIPELINES = {
    # 'scrapy_balloons.interceptors.PostInterceptor': 100,
    # 'scrapy_balloons.pipelines.ModifyProduct': 300,
    # 'scrapy_balloons.filters.PostFilters': 400,
    # 'scrapy_balloons.filters.StatsFilters': 500,

}

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/\
            537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
}

CONCURRENT_REQUESTS = 50
CONCURRENT_REQUESTS_PER_DOMAIN = 30
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 1000,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 123,
    'scrapy.contrib.feedexport.FeedExporter': None
}


DOWNLOAD_DELAY = 1


USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
        (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
