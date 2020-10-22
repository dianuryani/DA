import scrapy


class BabastudioSpider(scrapy.Spider):
    name = 'babastudio'
    allowed_domains = ['academy.babastudio.com']
    start_urls = ['http://academy.babastudio.com/']

    def parse(self, response):
        pass
