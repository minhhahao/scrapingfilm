# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class CrawlerItem(Item):
    product_name = Field()
    product_url = Field()
    name_vn = Field()
    name_en = Field()
    director = Field()
    film_star = Field()
    film_type = Field()
    film_genre = Field()
    film_status = Field()
    description = Field()
    country = Field()
    year = Field()
    sub = Field()
    ishd = Field()
    tags = Field()
    image_poster = Field()
