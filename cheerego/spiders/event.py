# -*- coding: utf-8 -*-
import scrapy


class EventSpider(scrapy.Spider):
    name = 'event'
    allowed_domains = ['cheerego']
    start_urls = ['http://cheerego.com/']

    def start_requests(self):
        for i in range(1, 2):
            yield scrapy.Request('http://cheerego.com/dome_web/event.php?pagenow=%s' % i)

    def parse(self, response):
        for item in response.css('.t11'):
            title = item.css('div.t18_red').xpath('text()').extract_first()
            print(title, item.xpath('node()').extract())

