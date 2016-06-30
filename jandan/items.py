# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JandanItem(scrapy.Item):
    image_urls = scrapy.Field()
    file_urls = scrapy.Field()
    
