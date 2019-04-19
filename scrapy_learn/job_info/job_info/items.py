# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()
    job_href = scrapy.Field()
    job_salary = scrapy.Field()
    job_info = scrapy.Field()
    company_name = scrapy.Field()
    company_info = scrapy.Field()
    job_des = scrapy.Field()

