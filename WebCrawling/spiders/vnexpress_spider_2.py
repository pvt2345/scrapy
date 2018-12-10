import scrapy
import json
import codecs
from scrapy import Selector

class VnexpressSpider_2(scrapy.Spider):
    name = "vnexpress_2"
    start_urls = [
    'https://thethao.vnexpress.net/tin-tuc/tin-tuc/hlv-park-hang-seo-canh-tinh-cau-thu-viet-nam-bang-bai-hoc-nam-2014-3849436.html'
    ]
    def parse(self, response):
        main = response.css('section')[3].css('div.section_container')[1].css('div.width_common')[1].css('div.left')[0].css(
            'div.width_common').xpath('//div[@id = "box_details_news"]')[0]
        # main = response.css('section')[3].xpath("//div[@id='box_details_news']")
        timestamp = main.css('header')[0].css('span::text').extract_first()
        title = main.css("div.title_news")[0].css("h1::text").extract_first()
        summary = main.css('h2::text').extract_first()
        related_news = main.css("div.relative_new ul li a::attr(href)").extract()
        listcontent = main.css("p::text").extract()[:-1]
        content = ''.join(item for item in listcontent)
        author = main.css("p strong::text")[-1].extract()


        a = {
            "timestamp" : timestamp,
            "title" : title,
            "summary" : summary,
            "related_news" : related_news,
            "content" : content,
            "author" : author
        }

        yield a