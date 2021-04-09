from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
from ..items import NewItem
from scrapy.loader import ItemLoader

class QuotesSpider(CrawlSpider):
    name = 'book2'
    print("hello")
    # allowed_domains = ['zingnews.vn']
    start_urls = ['https://zingnews.vn/the-thao.html']
    def parse(self, response):
        print('GSNFGIUONFDAVDFMVBEF')
        # Request tới từng sản phẩm có trong danh sách các dựa vào href
        for item_url in response.css('article header p.article-title a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_new) # Nếu có sản phẩm thì sẽ gọi tới function parse_new
        
    
    def parse_new(self, response):
        print('VDAFNMISIOSMANBIDF')
        item = NewItem()
        item['title']= response.css('h1.the-article-title::text').get()
        print(item['title'])
        item['des']= response.css('p.the-article-summary::text').get()
        yield item


        # exists = response.xpath('//article')
        # if exists:
        #     loader = ItemLoader(item=NewItem(), selector=response)
        #     loader.add_xpath('title', '//header/p/a/text()')
        #     loader.add_xpath('final_image',
        #                      '//p/a/img/@src')
        #     loader.add_xpath(
        #         'description', '//header/p[@class="article-summary"]/text()')
        #     loader.add_xpath(
        #         'href', '//header/p[@class="article-title"]/a/@href')
        #     yield loader.load_item()
        # else:
        #     print(response.url)




# import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "book"
#     start_urls = [
#         'https://zingnews.vn/the-thao.html'
#     ]

#     def parse(self, response):
#         for quote in response.css('article'):
#             yield {
#                 'title': quote.css('header p a::text').get(),
#                 'des': quote.css('header p.article-summary::text').get(),
#                 'href': quote.css('header p.article-title a::attr(href)').get(),
#             }