# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 抓標題
        print("------ 1 -------", response.xpath('//title'))
        print("------ 2 -------", response.xpath('//title').get())
        print("------ 3 -------", response.xpath('//title').extract())
        print("------ 4 -------", response.xpath('//title/text()').extract())
        print("------ 5 -------", response.xpath('//title/text()').extract()[0])

        # 抓作者
        sels = response.xpath('//div/span/small')
        for s in sels:
           print("=========", s.xpath('text()').extract()[0])

        # 抓格言 + 抓作者
        sels = response.xpath('//div[@class="quote"]')  # // 任何一層   //div 任何一層出現 div
        print("*******", len(sels))
        for s in sels:
            sent = s.xpath('span[@class="text"]/text()').extract()[0]
            author = s.xpath('span/small/text()').extract()[0]
            print("----------", author)
            print("--------------------", sent)

        # 將爬蟲結果存檔
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
