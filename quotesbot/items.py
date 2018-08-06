# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re

class QuotesbotItemTCM(scrapy.Item):
    # define the fields for your item here like:
    #中西药
    name = scrapy.Field()
    alias = scrapy.Field()
    medicinal_part = scrapy.Field()
    component = scrapy.Field()
    functional_management = scrapy.Field()
    usage_dosage = scrapy.Field()
    prescription = scrapy.Field()
    clinical_application = scrapy.Field()
    compatibility_incompatibility = scrapy.Field()
    # pass


class QuotesbotItemWM(scrapy.Item):
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
    # pass
