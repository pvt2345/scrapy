import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from WebCrawling.items import Author
# import json
class MySpider(CrawlSpider):
    name = 'crawlspider'
    allowed_domains = ['vnexpress.net']
    start_urls = ['https://vnexpress.net/tin-tuc/goc-nhin/tac-gia']

    rules = (
        Rule(LinkExtractor(allow=('/tac-gia/[0-9A-Za-z-]*.html')), callback='parse_item'),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        # Rule(LinkExtractor(allow=('/tac-gia/')), callback='parse_item')
    )


    def parse_item(self, response):
        # print("Hello world!")
        info = response.xpath('//p[@href="?"]/text()').extract_first()
        if(info is None):
            a = {
                  'name' : response.css(".author_name::text").extract_first().strip(),
                  'description' : response.css(".author_name span::text").extract_first().strip(),
                 }

            yield a
        else:
            a = {
                'name': response.css(".author_name::text").extract_first().strip(),
                'description': response.css(".author_name span::text").extract_first().strip(),
                'info' : info
            }

            yield a
        # l = ItemLoader(item=Author(), response=response)
        # l.add_css('name', '.author_name::text')
        # l.add_css('description', '.author_name span::text')
        # info = response.xpath('//p[@href="?"]/text()').extract_first()
        # if(info is not None):
        #     l.add_xpath('info','//p[@href="?"]/text()')
        # return l.load_item()