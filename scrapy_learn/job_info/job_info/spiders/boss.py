# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import requests
import random
from job_info.items import JobInfoItem
from job_info.settings import USER_AGENTS_LIST

from scrapy_redis.spiders import RedisSpider
class BossSpider(RedisSpider):
    """
    二、使用scrapy_redis进行分布式爬虫
    """
    name = 'boss'
    allowed_domains = ['zhipin.com']
    # start_urls = ['https://www.zhipin.com/c101190100-p100101/?ka=search_100101']
    redis_key = "boss"
    headers = {
        "user-agent": random.choice(USER_AGENTS_LIST)
    }

    def parse(self, response):
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
        next_url = response.xpath("//div[@class='page']/a[@class='next']/@href").extract_first()
        # print(next_url)
        if next_url:
            next_url= "https://www.zhipin.com" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,

            )

    def job_des(self, data_jid, data_lid):

        job_des_url = "https://www.zhipin.com/wapi/zpgeek/view/job/card.json?jid={}&lid={}".format(data_jid, data_lid)
        r = requests.get(job_des_url, headers=self.headers,timeout=5)
        data = r.json()["zpData"]["html"]
        data = etree.HTML(data)
        return data.xpath("//div[@class='detail-bottom-text']/text()")


"""
import scrapy
from lxml import etree
import requests
import random
from job_info.items import JobInfoItem
from job_info.settings import USER_AGENTS_LIST


class BossSpider(scrapy.Spider):

    # 一、爬取boss直聘JAVA页面信息，并存入表格或者redis数据库

    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101190100-p100101/?ka=search_100101']
    headers = {
        "user-agent": random.choice(USER_AGENTS_LIST)
    }

    def parse(self, response):
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
        next_url = response.xpath("//div[@class='page']/a[@class='next']/@href").extract_first()
        # print(next_url)
        if next_url:
            next_url= "https://www.zhipin.com" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,

            )

    def job_des(self, data_jid, data_lid):

        job_des_url = "https://www.zhipin.com/wapi/zpgeek/view/job/card.json?jid={}&lid={}".format(data_jid, data_lid)
        r = requests.get(job_des_url, headers=self.headers,timeout=5)
        data = r.json()["zpData"]["html"]
        data = etree.HTML(data)
        return data.xpath("//div[@class='detail-bottom-text']/text()")
"""
