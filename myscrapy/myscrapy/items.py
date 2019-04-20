# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    time = scrapy.Field()
    who = scrapy.Field()
    next_url = scrapy.Field()
    contents = scrapy.Field()
    contents_img = scrapy.Field()

