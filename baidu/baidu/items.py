# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    image_urls = scrapy.Field()
    image_type = scrapy.Field()
    images = scrapy.Field()
    #url = scrapy.Field()
    pass
