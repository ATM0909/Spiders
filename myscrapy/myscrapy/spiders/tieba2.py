# -*- coding: utf-8 -*-
import scrapy


class Tieba2Spider(scrapy.Spider):
    name = 'tieba2'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&mo_device=1&pn=0&']

    def parse(self, response):
        item = {}
        data = response.body.decode()
        # print(data)
        li_list = response.xpath("//li[@class=' j_thread_list clearfix']")
        print(li_list)
        # for li in li_list:
        #     item["title"] = li.xpath("./a/div[1]/span/text()").extract_first()
        #     item["href"] = li.xpath("./a/@href").extract_first()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        #     print(item)

