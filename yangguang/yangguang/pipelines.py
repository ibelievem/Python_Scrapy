# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道，处理数据

class YangguangPipeline(object):
    def process_item(self, item, spider):
        item["content"]=self.process_content(item["content"])

        print(item["content"])
        print(type(item["content"]))
        return item

    def process_content(self,content):
        for i in content:
            i.replace(r'\xa0\xa0\xa0\xa0',"").replace(r'\r\n      ','')

        return content
