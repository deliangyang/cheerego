# -*- coding: utf-8 -*-
import scrapy


class MessageSpider(scrapy.Spider):
    name = 'message'
    allowed_domains = ['cheerego.com']
    start_urls = ['http://cheerego.com/']

    def start_requests(self):
        for i in range(1, 2):
            yield scrapy.Request('http://cheerego.com/dome_web/guest_2016bbs.php?pagenow=%s' % i)

    def parse(self, response):
        for item in response.css('.messageBox'):
            image = item.css('.imgBox').xpath('img/@src').extract_first()
            node = item.css('.messageBox').xpath('node()').extract()
            user = item.css('.user').xpath('node()').extract()
            print(image, node, ''.join(user))
