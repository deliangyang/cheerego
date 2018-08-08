# -*- coding: utf-8 -*-
import scrapy


class OfficialSpider(scrapy.Spider):
    name = 'official'
    allowed_domains = ['cheerego.com']
    start_urls = ['http://cheerego.com/']

    def start_requests(self):
        yield scrapy.Request('http://cheerego.com/dome_web/bio.php')

    def parse(self, response):
        for item in response.css('.bioitemBox'):
            image = item.css('img').xpath('@src').extract_first()
            content = item.css('.t11_index_b').xpath('node()').extract()
            print(image, content)

#http://cheerego.com/dome_web/event.php?pagenow=3
#http://cheerego.com/dome_web/guest_2016bbs.php?pagerang=1&pagenow=3