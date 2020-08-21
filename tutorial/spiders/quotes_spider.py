import scrapy

class QuotesScraper(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
        'http://quotes.toscrape.com/page/2/'
    ]
    
