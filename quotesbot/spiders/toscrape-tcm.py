# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import QuotesbotItemTCM

# 抓取中药百科

class ToScrapeTCMSpider(scrapy.Spider):
    name = "toscrape-tcm"
    # start_urls = [
    #     'http://ypk.39.net/c516000/manual',
    # ]

    def parse(self, response):
        item = QuotesbotItemTCM()
        item["name"] = response.xpath('//div[@class="yps_top"]//div[@class="t1"]//h1/text()').extract_first().strip()
        #别名
        item["alias"] = response.xpath('//div[@id="tab2_con_2"]//dd/text()').extract_first()
        #药用部位
        item["medicinal_part"] = response.xpath('//div[@id="tab2_con_3"]//dd/text()').extract_first()
        #成分
        item["component"] = response.xpath('//div[@id="tab2_con_5"]//dd/text()').extract_first()
        #功能主治
        item["functional_management"] = response.xpath('//div[@id="tab2_con_6"]//dd/text()').extract_first()
        #用法与用量
        item["usage_dosage"] = response.xpath('//div[@id="tab2_con_7"]//dd/text()').extract_first()
        #选方
        item["prescription"] = response.xpath('//div[@id="tab2_con_8"]//dd/text()').extract_first()
        #临床应用
        item["clinical_application"] = response.xpath('//div[@id="tab2_con_9"]//dd/text()').extract_first()
        #宜忌
        item["compatibility_incompatibility"] = response.xpath('//div[@id="tab2_con_10"]//dd/text()').extract_first()
        return item
        # yield {
        #     #名称
        #     'name': response.xpath('//div[@class="yps_top"]//div[@class="t1"]//h1/text()').extract_first().strip(),
        #     #别名
        #     'alias': response.xpath('//div[@id="tab2_con_2"]//dd/text()').extract_first(),
        #     #药用部位
        #     'medicinal_part': response.xpath('//div[@id="tab2_con_3"]//dd/text()').extract_first(),
        #     #成分
        #     'component': response.xpath('//div[@id="tab2_con_5"]//dd/text()').extract_first(),
        #     #功能主治
        #     'functional_management': response.xpath('//div[@id="tab2_con_6"]//dd/text()').extract_first(),
        #     #用法与用量
        #     'usage_dosage': response.xpath('//div[@id="tab2_con_7"]//dd/text()').extract_first(),
        #     #选方
        #     'prescription': response.xpath('//div[@id="tab2_con_8"]//dd/text()').extract_first(),
        #     #临床应用
        #     'clinical_application': response.xpath('//div[@id="tab2_con_9"]//dd/text()').extract_first(),
        #     #宜忌
        #     'compatibility_incompatibility': response.xpath('//div[@id="tab2_con_10"]//dd/text()').extract_first()
        # }

    #通过使用循环来增加爬取网址
    def start_requests(self):
        pages=[]
        for i in range(4882, 4890):
            urls='http://ypk.39.net/c51%s/'%i
            page=scrapy.Request(urls)
            pages.append(page)
        return pages

        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
