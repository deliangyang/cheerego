# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MessageItem(scrapy.Item):
    username = scrapy.Field()
    avatar = scrapy.Field()
    message = scrapy.Field()
    create_at = scrapy.Field()


class EventItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    sort = scrapy.Field()


class AlbumItem(scrapy.Item):
    title = scrapy.Field()
    cover = scrapy.Field()
    description = scrapy.Field()
    release_time = scrapy.Field()
    release_company = scrapy.Field()
