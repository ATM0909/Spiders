# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 存入excel表格中
"""
from openpyxl import Workbook

class BookInfoPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['大分类', '中分类', '小分类', '小分类地址',
                        '书名', '作者', '出版社' ,'出版日期', '图书图片' ,
                        '图书地址' ,'价钱'])
    def process_item(self, item, spider):
        line = [item["b_cate"], item["m_cate"],item["s_cate"], item["s_cate_href"],
                item["book_name"],item["book_author"], item["book_publisher"], item["book_publish_date"],
                item["book_img"], item["book_href"], item["book_price"]]
        self.ws.append(line)
        self.wb.save("dangdang.xlsx")
        return item
"""


# 存入mongodb中
from pymongo import MongoClient
client = MongoClient()
collection = client["dangdang"]["book"]
class BookInfoPipeline(object):
    def process_item(self, item, spider):
        collection.insert(dict(item))

        return item

