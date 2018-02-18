# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaidubaikePipeline(object):
    def __init__(self):
        #if we use mongodb,we can init the link pool here
        pass
    def process_item(self, item, spider):
        data = item['data']
        filename = item['filename']
        with open(u"/data/yuliao/" + filename, 'a') as fp:
            fp.write(data)
        return item
    def __destory__(self):
        pass
