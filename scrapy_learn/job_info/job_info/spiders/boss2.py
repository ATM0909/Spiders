# -*- coding: utf-8 -*-
import scrapy
import requests
import random
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lxml import etree
from job_info.items import JobInfoItem
from job_info.settings import USER_AGENTS_LIST

class Boss2Spider(CrawlSpider):
    """
    -t crawl 实现自动翻页功能
    """
    name = 'boss2'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100-p100109/?ka=search_100109']
    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r"/c\d+-p\d+/\?page=\d+$"),callback='parse_item',follow=True),

    )
    headers = {
        "user-agent": random.choice(USER_AGENTS_LIST)
    }

    def parse_item(self, response):
        item=JobInfoItem()
        # item = {}
        li_list = response.xpath("//div[@class='job-list']/ul/li")
        for li in li_list:
            item["job_title"] = li.xpath("./div/div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract_first()
            item["job_href"] = li.xpath("./div/div[@class='info-primary']/h3/a/@href").extract_first()
            item["job_href"] ='https://www.zhipin.com'+ item["job_href"]
            item["job_salary"] = li.xpath("./div/div[@class='info-primary']/h3/a/span/text()").extract_first()
            item["job_info"] = li.xpath("./div/div[@class='info-primary']/p//text()").extract()
            item["job_info"] = " ".join(item["job_info"])

            item["company_name"] = li.xpath("./div/div[@class='info-company']/div/h3/a/text()").extract_first()
            item["company_info"] = li.xpath("./div/div[@class='info-company']/div/p//text()").extract()
            item["company_info"] = " ".join(item["company_info"])

            data_jid = li.xpath("./div/div[@class='info-primary']/h3/a/@data-jid").extract_first()
            data_lid = li.xpath("./div/div[@class='info-primary']/h3/a/@data-lid").extract_first()
            item["job_des"] = self.job_des(data_jid, data_lid)
            item["job_des"] = "".join(item["job_des"]).replace("\n", " ").strip()

            # print(item)
            yield item


    def job_des(self, data_jid, data_lid):

        job_des_url = "https://www.zhipin.com/wapi/zpgeek/view/job/card.json?jid={}&lid={}".format(data_jid, data_lid)
        r = requests.get(job_des_url, headers=self.headers,timeout=5)
        data = r.json()["zpData"]["html"]
        data = etree.HTML(data)
        return data.xpath("//div[@class='detail-bottom-text']/text()")
