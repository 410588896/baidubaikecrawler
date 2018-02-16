# -*- coding: utf-8 -*-
import scrapy


class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/']

    def parse(self, response):
        re_selector = response.xpath('//a/@href').extract()
        for url in re_selector:
            if url.find("http://") != -1 or url.find("https://") != -1:  #http:// https://
    
            else:    
