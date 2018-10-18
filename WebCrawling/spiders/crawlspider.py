import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json
class MySpider(CrawlSpider):
    name = 'crawlspider'
    allowed_domains = ['vnexpress.net']
    start_urls = ['https://vnexpress.net/tin-tuc/goc-nhin/tac-gia']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('/tac-gia/[0-9A-Za-z-]*.html')), callback='parse_item'),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        # Rule(LinkExtractor(allow=('/tac-gia/')), callback='parse_item')
    )
    #
    # def parse(self, response):
    #     self.logger.info('Hi, this is an item page! %s', response.url)
    #     # item = scrapy.Item()
    #     # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
    #     # item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
    #     # item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
    #     # item['name'] = response.css(".author_name::text").extract_first()
    #     try:
    #         sizebar_1 = response.css(".sidebar_2")[0]
    #         a = {'name': response.css(".author_name::text").extract_first().strip(),
    #              'description': response.css(".author_name span::text").extract_first().strip(),
    #              'info': sizebar_1.css("div").css("p").extract_first()
    #              }
    #
    #         filename = "D:/WebCrawling/tac-gia.json"
    #         with open(filename, 'a', encoding='utf-8') as f:
    #             json.dump(a, f)
    #     except:
    #         pass
    #
    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        # item = scrapy.Item()
        # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        # item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        # item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        # item['name'] = response.css(".author_name::text").extract_first()
        # sizebar_1 = response.css(".sidebar_2")[0]
        a = { 'name' : response.css(".author_name::text").extract_first().strip(),
              'description' : response.css(".author_name span::text").extract_first().strip(),
         # 'info' : sizebar_1.css("div").css("p").extract_first()
             }

        yield a
        # filename = "D:/WebCrawling/tac-gia.json"
        # with open (filename, 'a', encoding='utf-8') as f:
        #     json.dump(a, f)
        #
        # f.close()
        # yield item