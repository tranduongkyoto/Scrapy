import scrapy


class QuotesSpider(scrapy.Spider):
    name = "book"
    start_urls = [
        'https://zingnews.vn/the-thao.html'
    ]

    def parse(self, response):
        for quote in response.css('article'):
            yield {
                'title': quote.css('header p a::text').get(),
                'des': quote.css('header p.article-summary::text').get(),
                'href': quote.css('header p.article-title a::attr(href)').get(),
            }