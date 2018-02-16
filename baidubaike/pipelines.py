# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaidubaikePipeline(object):
    def __init__(self):
        #if we use mongodb,we can init the link pool here
        pass
    def process_item(self, item, spider):
        content = item['content']
        filename = item['filename']
        with open(filename, 'a') as fp:
            fp.write(content)
        return item
    def __destory__(self):
        pass
