# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PttmobileItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positive_count=scrapy.Field()
    negative_count=scrapy.Field()
    title=scrapy.Field()
    content_url=scrapy.Field()
    date=scrapy.Field()
    author=scrapy.Field()
    content=scrapy.Field()
    positive_user=scrapy.Field()
    negative_user=scrapy.Field()
   
    
