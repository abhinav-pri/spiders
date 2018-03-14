# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Restraunt(scrapy.Item):
    # define the fields for your item here like:
    link=scrapy.Field()
    typ=scrapy.Field()
    address=scrapy.Field() 
    rating=scrapy.Field()
    ZID=scrapy.Field()
    locality=scrapy.Field()
    name=scrapy.Field()
    Phone=scrapy.Field()
    piclinks=scrapy.Field()
    menu=scrapy.Field()
    price=scrapy.Field()
    category=scrapy.Field()
    item=scrapy.Field()
    VEG_OR_NONVEG=scrapy.Field()
    menu=scrapy.Field()
