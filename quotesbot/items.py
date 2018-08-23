# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#中药材
class QuotesbotItemTCM(scrapy.Item):
    #名称
    name = scrapy.Field()
    #类型
    type = scrapy.Field()
    #别名
    alias = scrapy.Field()
    #药用部位
    medicinal_part = scrapy.Field()
    #成分
    component = scrapy.Field()
    #功能主治
    functional_management = scrapy.Field()
    #用法与用量
    usage_dosage = scrapy.Field()
    #选方
    prescription = scrapy.Field()
    #临床应用
    clinical_application = scrapy.Field()
    #宜忌
    compatibility_incompatibility = scrapy.Field()

    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()

#中西成药
class QuotesbotItemWM(scrapy.Item):
    #名称
    name = scrapy.Field()
    #类型
    type = scrapy.Field()
    #成分
    component = scrapy.Field()
    #功能主治
    functional_management = scrapy.Field()
    #用法与用量
    usage_dosage = scrapy.Field()
    #药理作用
    pharmacological = scrapy.Field()
    #宜忌
    compatibility_incompatibility = scrapy.Field()
    #不良反应
    adverse_reactions = scrapy.Field()
    #注意事项
    matters = scrapy.Field()

    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field() #存放图片名字
    