# -*- coding: utf-8 -*-
import scrapy


class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/']

    def parse(self, response):
        #re_selector = response.xpath('//title/text()')
        print(response.text)
