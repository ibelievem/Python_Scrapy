# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# DTO 数据传输对象
class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName = scrapy.Field()
    companyName = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()
    date = scrapy.Field()
