# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from myscrapy.items import MyscrapyItem
class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, "lxml")
        data = soup.find("table", class_="tablelist")

        trs = data.select("tr")

        for tr in trs[1:-2]:
            td = tr.select("td")
            item =MyscrapyItem()

            item["title"] = td[0].string
            item["position"] = td[3].string
            item["date"] = td[4].string

            yield item





        div = soup.find('div', class_="pagenav")
        next = div.find("a" , id="next")
        next_url = next['href']
        # print(next_url)
        next_url = "https://hr.tencent.com/" + next_url
        yield scrapy.Request(
            next_url,
            callback=self.parse
        )


