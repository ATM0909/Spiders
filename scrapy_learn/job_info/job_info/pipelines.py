# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class JobInfoPipeline(object):

    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['工作名', '工作网址', '薪水' ,'信息',
                        '公司' ,'公司信息' ,'职责描述'])

    def process_item(self, item, spider):
        """
        对item数据进行处理
        """

        line = [item["job_title"],item["job_href"], item["job_salary"],
                item["job_info"],
                item["company_name"], item["company_info"], item["job_des"]]
        self.ws.append(line)
        self.wb.save("JAVA.xlsx")
        # print(item)
        return item
