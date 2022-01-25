import scrapy


class GetreviewsSpider(scrapy.Spider):
    name = 'getreviews'
    allowed_domains = ['https://shopee.vn/']
    start_urls = ['http://https://shopee.vn//']

    def parse(self, response):
        pass
