# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    name = scrapy.Field()
    tag = scrapy.Field()
    time = scrapy.Field()
