# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
from quotesbot.items import QuotesbotItemTCM
from quotesbot.items import QuotesbotItemWM


class QuotesbotPipeline(object):
    def __init__(self):
        pass
        # if isinstance(item, QuotesbotItemTCM):
        #     self.file0 = open('data_tcm.json', 'w', encoding='utf-8')
        # if isinstance(item, QuotesbotItemWM):
        #     self.file1 = open('data_wm.json', 'w', encoding='utf-8')

    def open_spider(self, spider):
        if(spider.name=='toscrape-tcm'):
            self.file0 = open('data_tcm.json', 'w', encoding='utf-8')
        elif(spider.name=='toscrape-wm'):
            self.file1 = open('data_wm.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        if(spider.name=='toscrape-tcm'):
            self.file0.close()
        elif(spider.name=='toscrape-wm'):
            self.file1.close()

    def process_item(self, item, spider):
        #根据抓取数据类型输出到不同文件中
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
                #丢弃掉名称为空值的数据
                raise DropItem("Missing name in %s" % item)            
