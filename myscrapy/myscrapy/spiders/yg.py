# coding: utf-8
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import chardet
class YgSpider(CrawlSpider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    # start_urls = ['http://wz.sun0769.com/']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'http://wz.sun0769.com/index.php/question/questionType?page=30'),  follow=True),
        Rule(LinkExtractor(allow=r'http://(d\.)?wz.sun0769.com/(index\.php|html)/question/(\d+/\d+\.shtml|show?id=\d+)'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'http://wz.sun0769.com/index.php/question/(report|questionType)\?page=\d+'),  follow=True),

    )

    def parse_item(self, response):

        # encode_type = chardet.detect(response.body)

        item = {}
        item["title"] = re.findall(r"<span class=\"niae2_top\">提问：(.*?)</span>", response.body.decode(encoding='gbk'))[0]
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        print(item)
