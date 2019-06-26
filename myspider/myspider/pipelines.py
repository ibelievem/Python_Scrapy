# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道，保存数据


class MyspiderPipeline(object):

    # 初始化
    def __init__(self):
        self.file = open("./teacher.csv","w",encoding="utf-8")
        self.file.write("name"+","+"title"+"\n")

    # 处理数据对象
    def process_item(self, item, spider):
        self.file.write(item["name"] + "," + item["title"] + "\n")
        return item

    # 结束化
    def close_spider(self, spider):
        self.file.close()
