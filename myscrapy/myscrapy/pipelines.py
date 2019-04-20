# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
logger = logging.getLogger(__name__)
from pymongo import MongoClient

client = MongoClient()
collection = client["suning"]["book"]


class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        collection.insert(dict(item))

        return item


class RedisPipeline(object):
    def process_item(self, item, spider):  # 实现数据的保存


        return deferToThread(self._process_item, item, spider)  # 调用异步线程去处理item

    def _process_item(self, item, spider):

        key = self.item_key(item, spider)
        data = self.serialize(item)
        self.server.rpush(key, data)  # 向items中添加item
        return item