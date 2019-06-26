# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    # 爬虫名(爬虫启动时候使用：scrapy crawl itcast)
    name = 'itcast'

    # 允许爬取的范围,防止爬虫爬到了别的网站
    allowed_domains = ['incast.cn']

    # 开始爬取的url地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']


    # 数据提取方法，接收下载中间件传过来的start_urls地址对应的响应
    def parse(self, response):
        # response.xpath()返回的是一个含有selector对象的列表
        # ret1 = response.xpath("//div[@class='tea_con']//h30/text()").extract()
        # 返回包含选择器的列表
        # print(ret1)

        # 分组
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = MyspiderItem()

            # 使用items定义好字段，防止这里因字段写错而存储到错误的字段中。
            # 因为字段错误会拒绝执行
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            # Request, BaseItem, dict or None

            yield item




