# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import QuotesbotItemWM

# 抓取中西成药百科
# 抓取网址在start_request中定义

class ToScrapeWMSpider(scrapy.Spider):
    name = "toscrape-wm"

    def parse(self, response):
        item = QuotesbotItemWM()
        #名称
        item["name"] = response.xpath('//div[@class="instruction"]//dl[1]//a/text()').extract_first()
        #类型
        item["type"] = response.xpath('//div[@class="crumb"]/ul/li[4]//span/text()').extract_first()
        #成分
        item["component"] = response.xpath('//div[@class="instruction"]//dl[2]//dd/text()').extract_first().strip()
        #功能主治
        item["functional_management"] = response.xpath('//div[@class="instruction"]//dl[3]//dd/text()').extract_first().strip()
        #用法与用量
        item["usage_dosage"] = response.xpath('//div[@class="instruction"]//dl[4]//dd/text()').extract_first().strip()
        #药理作用
        item["pharmacological"] = response.xpath('//div[@class="instruction"]//dl[5]//dd/text()').extract_first().strip()
        #宜忌
        item["compatibility_incompatibility"] = response.xpath('//div[@class="instruction"]//dl[6]//dd/text()').extract_first().strip()
        #不良反应
        item["adverse_reactions"] = response.xpath('//div[@class="instruction"]//dl[7]//dd/text()').extract_first().strip()
        #注意事项
        item["matters"] = response.xpath('//div[@class="instruction"]//dl[8]//dd/text()').extract_first().strip()
        return item

    #通过使用循环来增加爬取网址
    def start_requests(self):
        pages=[]
        for i in range(2802, 6000):
            urls='http://www.12yao.com/baike/%s/detailed'%i
            page=scrapy.Request(urls)
            pages.append(page)
        return pages
