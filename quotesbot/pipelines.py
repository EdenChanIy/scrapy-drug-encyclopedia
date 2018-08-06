# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
from quotesbot.items import QuotesbotItemWM
from quotesbot.items import QuotesbotItemTCM

#中西药
class QuotesbotPipeline(object):
    def __init__(self):
        self.file0 = open('test0.json', 'w', encoding='utf-8')
        self.file1 = open('test1.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item, QuotesbotItemTCM):
            lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.file0.write(lines)
            return item
        if isinstance(item, QuotesbotItemWM):
            if item['name']:
                lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
                self.file1.write(lines)
                return item
            else:
                raise DropItem("Missing name in %s" % item)            
