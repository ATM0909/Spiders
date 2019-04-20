# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from book_info.items import BookInfoItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://book.dangdang.com/']

    def parse(self, response):
        div_list = response.xpath("//div[@class='con flq_body']/div")
        for div in div_list:
            # item = {}
            item = BookInfoItem()
            item["b_cate"] = div.xpath("./dl/dt//text()").extract()
            item["b_cate"] = [i.strip() for i in item["b_cate"] if len(i.strip()) > 0][0]
            dl_list = div.xpath("./div//dl[@class='inner_dl']")
            for dl in dl_list:
                item["m_cate"] = dl.xpath("./dt//text()").extract()
                item["m_cate"] = [i.strip() for i in item["m_cate"] if len(i.strip()) > 0][0]
                a_list = dl.xpath("./dd/a")
                for a in a_list:
                    item["s_cate"] = a.xpath("./@title").extract_first()
                    item["s_cate_href"] = a.xpath("./@href").extract_first()
                    # print(item)
                    if item["s_cate_href"] :
                        yield scrapy.Request(
                            item["s_cate_href"],
                            callback=self.book_page_list,
                            meta={"item":deepcopy(item)}
                        )

    def book_page_list(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@id='component_59']/li")
        for li in li_list:
            item["book_name"] = li.xpath("./a/@title").extract_first()
            item["book_href"] = li.xpath("./a/@href").extract_first()
            item["book_img"] = li.xpath("./a/img/@src").extract_first()
            if item["book_img"]=='images/model/guan/url_none.png':
                item["book_img"]= li.xpath("./a/img/@data-original").extract_first()
            item["book_price"] = li.xpath("./p[@class='price']/span[1]/text()").extract_first()
            item["book_author"] = li.xpath("./p[@class='search_book_author']/span[1]/a[1]/@title").extract_first()
            item["book_publish_date"] = li.xpath("./p[@class='search_book_author']/span[2]/text()").extract_first()
            item["book_publisher"] = li.xpath("./p[@class='search_book_author']/span[3]/a/@title").extract_first()
            yield item
            # print(item)
        next_url = response.xpath("//div[@class='paging']/ul/li[@class='next']/a/@href").extract_first()
        if next_url:
            next_url = 'http://category.dangdang.com/'+next_url
            yield scrapy.Request(
                next_url,
                callback=self.book_page_list,
                meta={"item":item}
            )
