import scrapy

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()

