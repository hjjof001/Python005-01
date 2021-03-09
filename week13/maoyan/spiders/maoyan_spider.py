import scrapy
from scrapy.selector import Selector

from maoyan.items import MaoyanItem


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    allowed_domains = ['maoyan.com']
    start_urls = []

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        movies_array = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies_array:
            item = MaoyanItem()
            item['name'] = movie.xpath('./div/@title').extract_first()
            item['tag'] = movie.xpath('./div[2]/text()[2]').extract_first().replace('\n', '').strip()
            item['time'] = movie.xpath('./div[4]/text()[2]').extract_first().replace('\n', '').strip()
            yield item
