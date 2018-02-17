# -*- coding: utf-8 -*-
import scrapy
from redis import StrictRedis
from .settings import REDIS_URL

class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/']
    redis_conn = StrictRedis.from_url(REDIS_URL)

    def parse(self, response):
        re_selector = response.xpath('//a/@href').extract()
        for url in re_selector:
            if url.find("http://") == -1 and url.find("https://") == -1:  #http:// https://
                url = "https://baike.baidu.com" + url    
            if url.find("#") != -1:
                url = url.split("#")[0]
        ad
