import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        page = "Extract text, author and tags"
        quotes = response.css("div.quote")
        for quote in quotes:
            yield {
                'text' : quote.css("span.text::text").extract_first(),
                'author':  quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags a.tag::text").extract()
            }
