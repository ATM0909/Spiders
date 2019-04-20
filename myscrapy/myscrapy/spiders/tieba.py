# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TiebaSpider(CrawlSpider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&mo_device=1&pn=0&']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = {}
        li_list = response.xpath("//li[contains(@class, 'tl_shadow tl_shadow_new')").extract()
        for li in li_list:
            item["title"] = li.xpath("/a/div[1]/span/text()").extract_first()
            item["herf"] = li.xpath("/a/@herf").extract_first()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
            print(item)
