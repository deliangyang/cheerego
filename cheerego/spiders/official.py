# -*- coding: utf-8 -*-
import scrapy
import re
from utils.common import strip_tags
from cheerego.items import AlbumItem


class OfficialSpider(scrapy.Spider):
    name = 'official'
    allowed_domains = ['cheerego.com']
    start_urls = ['http://cheerego.com/']

    def start_requests(self):
        yield scrapy.Request('http://cheerego.com/dome_web/bio.php')

    def parse(self, response):
        for item in response.css('.bioitemBox'):
            image = item.css('img').xpath('@src').extract_first()
            content_node = item.css('.t11_index_b').xpath('node()').extract()
            content = ''.join(content_node)

            item = AlbumItem()
            item['cover'] = 'http://cheerego.com/dome_web/%s' % image
            match = re.findall(r'發行公司:([^<]+)', content)
            item['release_company'] = ''
            if match:
                item['release_company'] = match[0]

            match = re.findall(r'發行日期:(\d+)年(\d+)月', content)
            item['release_time'] = ''
            if match:
                year, month = match[0]
                item['release_time'] = '%s-%s' % (year, month)

            item['title'] = strip_tags(re.sub(r'發行.+$', '', content))
            item['title'] = re.sub(r'\n', ' ', item['title'])
            item['title'] = re.sub(r'\s{2,}', ' ', item['title']).strip()

            yield item

        for item in response.css('.sectionText'):
            year = item.xpath('p/text()').extract_first()
            theme = item.xpath('h2/text()').extract()
            events = []
            for event in item.css('ul'):
                events.append(event.xpath('li/text()').extract())

            print(year, theme, events)
