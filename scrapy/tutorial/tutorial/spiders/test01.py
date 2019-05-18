# -*- coding: utf-8 -*-
import scrapy

# 改成 https 失敗
class Test01Spider(scrapy.Spider):
    name = 'test01'
    allowed_domains = ['ruten.com.tw']
    start_urls = ['https://clss.ruten.com.tw/category/']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
