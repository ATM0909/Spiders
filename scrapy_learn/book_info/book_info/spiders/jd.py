# -*- coding: utf-8 -*-
import scrapy
import copy
import json
import requests
from book_info.settings import USER_AGENT

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com', 'p.3.cn', 'rms.shop.jd.com']
    start_urls = ['https://book.jd.com/booksort.html']
    headers = {
            "user-agent": USER_AGENT
        }

    def parse(self, response):

        item={}
        dt_list = response.xpath("//div[@class='mc']/dl/dt")

        for dt in dt_list:
            item["b_cast"] = dt.xpath("./a/text()").extract_first()

            em_list = dt.xpath("./following-sibling::dd[1]/em")
            for em in em_list:
                item["s_cast"] = em.xpath("./a/text()").extract_first()
                item["s_cast_href"] = em.xpath("./a/@href").extract_first()
                item["s_cast_href"] = "https:"+ item["s_cast_href"]
                # print(item)
                yield scrapy.Request(
                    item["s_cast_href"],
                    callback= self.book_page,
                    meta={"item":copy.deepcopy(item)}  # 防止item覆盖，所以使用深拷贝
                )


    def book_page(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class='gl-warp clearfix']/li")
        for li in li_list:
            book_sku = li.xpath("./div/@data-sku").extract_first()
            venderId = li.xpath("./div/@venderid").extract_first()
            item["shop"] = self.book_shop_url(venderId)
            item["price"] = self.book_price_url(book_sku)

            item["book_name"] = li.xpath("./div/div[3]/a/em/text()").extract_first()
            item["author"] = li.xpath("./div/div[@class='p-bookdetails']/span[@class='p-bi-name']//a/@title").extract_first()

            print(item)


        # 获取下一页
        # next_url = response.xpath("//a[contains(text(), '下一页')]/@href").extract_first()
        # # print(next_url)
        # if next_url:
        #     next_url = 'https://list.jd.com/' + next_url
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.book_page,
        #         meta={"item": response.meta["item"]}
        #     )

        # yield item
    def book_price_url(self, book_sku):
        book_price_url = "https://p.3.cn/prices/mgets?skuIds=J_{}".format(book_sku)
        r = requests.get(book_price_url,headers=self.headers)
        r.raise_for_status()
        return json.loads(r.content.decode())[0]["op"]


    def book_shop_url(self, venderId):
        book_shop_url = "https://rms.shop.jd.com/json/pop/shopInfo.action?ids={}".format(venderId)
        r = requests.get(book_shop_url ,headers=self.headers)
        r.raise_for_status()
        return json.loads(r.content.decode(encoding='gbk'))[0]["name"]
