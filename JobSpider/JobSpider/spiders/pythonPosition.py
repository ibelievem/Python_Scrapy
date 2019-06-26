# -*- coding: utf-8 -*-
import scrapy
from ..items import JobspiderItem
from scrapy.http.response import Response
from scrapy.http.request import Request
from scrapy.selector.unified import SelectorList
from time import sleep
import random

class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    #allowed_domains = ['xxx']

    page = 1
    url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,{0}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    start_urls = [url.format(str(page))]

    # 传递下载器的请求结果 信息包含在参数response
    def parse(self, response):

        print(response.body)
        print("应答对象信息",response)
        print("应答对象类型", type(response))

        # 通过css选择器获取
        # response.css
        # 通过正则获取
        # response.re

        # 取所有岗位信息
        job_list = response.xpath("//div[@class='dw_table']/div[@class='el']")
        # 再从每一条岗位信息 通过 . 操作代表当前节点 往下找
        for each in job_list:
            positionName = each.xpath("normalize-space(./p/span/a/text())").extract()[0]

            #from scrapy.selector.unified import SelectorList
            # scrapy 把xpath提取的结果封装到SelectorList
            # extract()返回一个列表
            # print("xpath结果对象信息",positionName)
            # print("xpath结果对象类型", type(positionName))

            city = each.xpath("./span[@class='t3']/text()").extract()[0]
            date = each.xpath(".//span[@class='t5']/text()").extract()[0]
            salary = each.xpath(".//span[@class='t4']/text()").extract()
            if len(salary) > 0:
                salary = salary[0]
            else:
                salary = ''

            # 管道需要的数据对象
            item = JobspiderItem()
            item['positionName'] = positionName
            item['city'] = city
            item['date'] = date
            item['salary'] = salary
            # 将获取的数据交给pipeline
            yield item

        # 当页面没有工作信息的时候  结束翻页
        if(len(job_list) != 0):
            self.page = self.page + 1
            print("爬取页码：",str(self.page))
            yield Request(self.url.format(self.page),self.parse)

