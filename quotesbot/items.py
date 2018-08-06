# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    #中西药
    name = scrapy.Field()
    component = scrapy.Field()
    functional_management = scrapy.Field()
    usage_dosage = scrapy.Field()
    pharmacological = scrapy.Field()
    compatibility_incompatibility = scrapy.Field()
    adverse_reactions = scrapy.Field()
    matters = scrapy.Field()
    pass
