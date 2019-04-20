# -*- coding: utf-8 -*-
import scrapy


import logging
logger = logging.getLogger(__name__)
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee'] # 最开始请求的url

    def parse(self, response):
        # 处理url的响应， 不可更改函数名
        # ret = response.xpath("//div[@class='tea_con']//h3/text()")

        # print(ret)
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            item['name']=li.xpath(".//h3/text()").extract_first()
            item['title']=li.xpath(".//h4/text()").extract_first()
            logger.warning(item)
            yield item
