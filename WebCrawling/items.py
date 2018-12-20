# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class Author(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())
    info = scrapy.Field(output_processor=TakeFirst())

class File_Item(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()