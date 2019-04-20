# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from myscrapy.items import MyscrapyItem
from copy import deepcopy

class YangguangSpider(scrapy.Spider):
    name = 'yangguang'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType']

    def parse(self, response):
        item = MyscrapyItem()
        tr_list = response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
        for tr in tr_list:
            item["title"] = tr.xpath("./td[2]/a[@class='news14']/@title").extract_first()
            item["href"] = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item["who"] = tr.xpath("./td[4]/text()").extract_first()
            item["time"] = tr.xpath("./td[5]/text()").extract_first()

            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                meta={"item": deepcopy(item)}
            )
        next_url = response.xpath("//div[@class='pagination']/a[@text()='>']/@href").extract_first()
        if next_url is not None:

            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
        yield item
    def parse_detail(self, response):
        item = response.meta["item"]
        item["contents"] = response.xpath("//div[@class='wzy1']/table[2]//td[@class='txt16_3']/text()").extract()
        item["contents_img"] = response.xpath("//div[@class='textpic']/img/@src").extract()
        item["contents_img"] = ["http://wz.sun0769.com" + i for i in item["contents_img"]]
        # yield item
        return item



