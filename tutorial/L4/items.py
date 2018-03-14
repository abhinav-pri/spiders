# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Restraunt(scrapy.Item):
    # define the fields for your item here like:
    Link=scrapy.Field()
    typ=scrapy.Field()
    Address=scrapy.Field() 
    Rating=scrapy.Field()
    ZID=scrapy.Field()
    Locality=scrapy.Field()
    Name=scrapy.Field()
    Phone=scrapy.Field()
    piclinks=scrapy.Field()
    item=scrapy.Field()
    category=scrapy.Field()
    price=scrapy.Field()
   
