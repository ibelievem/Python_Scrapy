# -*- coding: utf-8 -*-
import scrapy
from ..items import YangguangItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    # 域名
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        # 分组
        tr_list=response.xpath('//div[@class="greyframe"]/table[2]/tr/td/table/tr')

        for  i in tr_list:
            item=YangguangItem()
            item["title"]=i.xpath('./td[2]/a[@class="news14"]/@title').extract_first()
            item["href"]=i.xpath('./td[2]/a[@class="news14"]/@href').extract_first()
            item["publish_date"]=i.xpath('./td[last()]/text()').extract_first()

            yield scrapy.Request(
                item["href"],

                # 指定传入的url交给那个解析函数去处理
                callback=self.parse_detail,

                # 实现不同解析函数中传递数据
                meta={"item":item}
            )


        # 翻页，并且获取详情页的相关数据
        next_url=response.xpath('//a[text()=">"]/@href').extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )


    # 处理详情页
    def parse_detail(self,reponse):
        item=reponse.meta["item"]
        item["content"]=reponse.xpath('//td[@class="txt16_3"]/text()').extract()
        item["content_img"]=reponse.xpath('//td[@class="txt16_3"]//img/@src').extract()
        if len(item["content_img"]) > 0:
            item["content_img"] = item["content_img"][0]
            item["content_img"] = ["http://wz.sun0769.com"+item["content_img"]]
        else:
            item["content_img"] = ''

        yield item

