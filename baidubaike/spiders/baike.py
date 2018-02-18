# -*- coding: utf-8 -*-
import scrapy
from redis import StrictRedis
from ..settings import REDIS_URL
from baidubaike import items

class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/']
    redis_conn = StrictRedis.from_url(REDIS_URL)

    def parse(self, response):
        if response.url.find("baike.baidu.com") != -1:
            re_selector = response.xpath('//a/@href').extract()
            for url in re_selector:
                if url.find("javascript") != -1:
                    continue
                if url.find("http://") == -1 and url.find("https://") == -1:  #http:// https://
                    url = "https://baike.baidu.com" + url    
                if url.find("#") != -1:
                    url = url.split("#")[0]
                if url.find("baike.baidu.com") != -1:
                    if self.redis_conn.sadd("start_urls", url) != 0:
                        self.redis_conn.rpush("wait_queue", url)

        item = items.BaidubaikeItem()
        item['url'] = response.url
        item['filename'] = response.xpath('/html/head/title/text()').extract()[0] 
        item['data'] = ''
        info = response.xpath('//div[@class="para"]')
        content = info.xpath('string(.)').extract()
        for data in content:
            item['data'] += data
        yield item
        yield scrapy.Request(self.redis_conn.lpop("wait_queue"), callback=self.parse, dont_filter = True)
