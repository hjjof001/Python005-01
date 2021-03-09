import scrapy
from scrapy.selector import Selector

from maoyan.items import MaoyanItem


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board']

    def parse(self, response):
        item = MaoyanItem()
        movies = Selector(response=response).xpath('//div[@class="movie-item-info"]')
        for movie in movies:
            item["name"] = movie.xpath('.//a/text()').extract_first().strip()
            item["type"] = movie.xpath('./p[@class="star"]/text()').extract_first().strip()
            item["time"] = movie.xpath('./p[@class="releasetime"]/text()').extract_first().strip()
            yield item
