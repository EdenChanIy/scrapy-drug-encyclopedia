# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import QuotesbotItemWM

# 抓取中西药

class ToScrapeWMSpider(scrapy.Spider):
    name = "toscrape-wm"
    # start_urls = [
    #     'http://ypk.39.net/c516000/manual',
    # ]

    def parse(self, response):
        item = QuotesbotItemWM()
        item["name"] = response.xpath('//div[@class="instruction"]//dl[1]//a/text()').extract_first()
        item["component"] = response.xpath('//div[@class="instruction"]//dl[2]//dd/text()').extract_first().strip()
        return item
        # yield {
        #     #名称
        #     'name': response.xpath('//div[@class="instruction"]//dl[1]//a/text()').extract_first(),
        #     #成分
        #     'component': response.xpath('//div[@class="instruction"]//dl[2]//dd/text()').extract_first().strip(),
        #     #功能主治
        #     'functional_management': response.xpath('//div[@class="instruction"]//dl[3]//dd/text()').extract_first().strip(),
        #     #用法与用量
        #     'usage_dosage': response.xpath('//div[@class="instruction"]//dl[4]//dd/text()').extract_first().strip(),
        #     #药理作用
        #     'pharmacological': response.xpath('//div[@class="instruction"]//dl[5]//dd/text()').extract_first().strip(),
        #     #宜忌
        #     'compatibility_incompatibility': response.xpath('//div[@class="instruction"]//dl[6]//dd/text()').extract_first().strip(),
        #     #不良反应
        #     'adverse_reactions': response.xpath('//div[@class="instruction"]//dl[7]//dd/text()').extract_first().strip(),
        #     #注意事项
        #     'matters': response.xpath('//div[@class="instruction"]//dl[8]//dd/text()').extract_first().strip()

        # }

    #通过使用循环来增加爬取网址
    def start_requests(self):
        pages=[]
        for i in range(2802, 2810):
            urls='http://www.12yao.com/baike/%s/detailed'%i
            page=scrapy.Request(urls)
            pages.append(page)
        return pages

        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
