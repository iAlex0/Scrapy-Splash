# spiders/quotes.py
import scrapy
from main_scraper.items import QuoteItem

from scrapy_splash import SplashRequest 

class QuotesSpider(scrapy.Spider):
    name = 'wait_time'

    def start_requests(self):
        url = 'https://quotes.toscrape.com/js/'
        yield SplashRequest(url, callback=self.parse, args={'wait': 0.5})

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
