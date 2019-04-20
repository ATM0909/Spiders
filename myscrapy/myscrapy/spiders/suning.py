# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import json

# 继承自RedisSpider
from scrapy_redis.spiders import RedisSpider

class SuningSpider(RedisSpider):

    redis_key ="suning"
    name = 'suning'
    allowed_domains = ['book.suning.com']
    # start_urls = ['https://book.suning.com/?safp=d488778a.10038.0.8cca61ce53']

    def parse(self, response):
        """
        获取苏宁图书的所有图书大标题分类与小标题分类
        Beautifulsoup 一种操作

        """
        # menu_subs = response.xpath("//div[@class='menu-list']/div[@class='menu-sub']")
        data = response.body
        soup = BeautifulSoup(data, "lxml")
        menu_subs = soup.select(".menu-list  div[class=menu-sub] ")
        for menu_sub in menu_subs:
            item={}
            b_cast_list = menu_sub.select(".submenu-left p")
            for b_casts in b_cast_list:
                b_cast= b_casts .select("a")      # 所有大标题节点 列表

                for b_title in b_cast:
                    # 大标题
                    item["b_title"] = b_title.get_text()
                    # 小标题的父节点的后面节点
                    s_casts = b_title .parent.find_next_sibling()  # ul列表

                    for s_cast in s_casts:

                        if s_casts.index(s_cast)%2 != 0:  # ul下节点有字符串
                            item["s_title"] = s_cast.select("li a")[0].get_text()
                            print(item)

    # def parse(self, response):
    #     """
    #     获取苏宁图书的所有图书大标题分类与小标题分类
    #     xpath 二种操作
    #
    #     """
    #     menu_subs = response.xpath("//div[@class='menu-list']/div[@class='menu-sub']")
    #
    #     for menu_sub in menu_subs:
    #         item={}
    #         b_cast_list = menu_sub.xpath("./div[1]/p")
    #         # print(b_cast_list)
    #         for b_casts in b_cast_list:
    #
    #             b_cast_a= b_casts .xpath("./a")    # 所有大标题节点 列表
    #             # b_cast= b_casts .xpath("./a/text()").extract_first()     # 所有大标题节点 列表
    #             # print(b_cast_a)
    #
    #             # print(b_cast)
    #             for b_title in b_cast_a:
    #                 #     # 大标题
    #                 item["b_title"] = b_title.xpath("./text()").extract_first()
    #                 # b_title = b_title.xpath("./text()").extract_first()
    #                 # print(b_title)
    #
    #                 # 小标题的父节点的后面节点
    #                 s_casts = b_title .xpath("../following-sibling::ul[1]") # ul列表
    #                 # print(s_casts)
    #                 for s_cast in s_casts:
    #                     """
    #                     一种方法
    #                     """
    #                     # s_titles = s_cast.xpath("./li/a/text()").extract()
    #                     # for s_title in s_titles:
    #                     #     item["s_title"] = s_title
    #                     #     print(item)
    #
    #                     """
    #                     二种方法
    #                     """
    #
    #                     s_titles = s_cast.xpath("./li/a/text()").extract()
    #                     item["s_title"] = s_titles
    #                     print(item)






    # def s_cast_detail(self, response):
    #     item = response.meta["item"]
    #     data = response.body
    #     soup = BeautifulSoup(data, "lxml")
    #     li_list = soup.select("#filter-results ul li ")
    #     # print(li_list[0])
    #     for li in li_list:
    #         # print(list[0])
    #
    #         book_img= li.select(".wrap div[class='res-img'] div[class='img-block']  img[class='search-loading']")[0]
    #         # print(book_img)
    #         item['book_img'] = book_img['src2']
    #         item['book_title'] = book_img['alt']
    #         book_price = li.select(".wrap div[class='res-info']  p[class='seller oh no-more'] a ")[0]
    #         # book_price = response.xpath("div.res-info > p.seller.oh.no-more ")
    #         # print(book_price)
    #         # item['book_price'] = book_price.get_text()
    #         yield item



