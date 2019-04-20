# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from bs4 import BeautifulSoup


from scrapy_redis.spiders import RedisCrawlSpider
class Suning2Spider(RedisCrawlSpider):
    redis_key = "sining"
    name = 'suning2'
    allowed_domains = ['book.suning.com']
    # start_urls = ['http://book.suning.com']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'https://list.suning.com/\d+-\d+-\d+\.html'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'https://list.suning.com/1-502680-0.html'), callback='parse_item'),
    )



    def parse_item(self, response):

        data = response.body
        soup = BeautifulSoup(data, "lxml")
        li_list = soup.select("#filter-results ul li ")
        print(li_list)
        # for li in li_list:
        #     # print(list[0])
        #     item = {}
        #     book_img= li.select(".wrap div[class='res-img'] div[class='img-block']  img[class='search-loading']")[0]
        #     # print(book_img)
        #     item['book_img'] = book_img['src2']
        #     item['book_title'] = book_img['alt']
        #
        # # item["href"] = re.findall(r"<img class=\"search-loading\" alt=\".*\" width=\"220\" height=\"220\" src=\"(.*?)\"", response.body.decode(encoding='gbk'))[0]
        # # item["href"] = re.findall(r"https://list.suning.com/\d+-\d+-\d+\.html", response.body.decode(encoding='gbk'))[0]
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        #     print(item)
