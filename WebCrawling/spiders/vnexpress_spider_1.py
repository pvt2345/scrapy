import scrapy
import json
import codecs
from scrapy import Selector

class VnexpressSpider_1(scrapy.Spider):
    name = "vnexpress_1"
    def __init__(self):
        super(VnexpressSpider_1, self).__init__()
        self.start_urls = [
            'https://vnexpress.net/tin-tuc/the-gioi/giam-doc-huawei-bi-bat-co-7-cuon-ho-chieu-3851640.html'
        ]

    def parse(self, response):
        # page = response.url.split("/")[-1]
        # page = page.split(".")[0]
        body = response.css("body")[0]
        section = body.css("section.container")[0]
        subsection = section.css("section.wrap_sidebar_12")[0]
        subsection_ = subsection.css("section.sidebar_1")[0]
        timestamp =  subsection_.css("header.clearfix span::text").extract_first()
        title = subsection_.css("h1::text").extract_first().strip()
        description = subsection_.css("h2::text").extract_first().strip()
        related_news_ = subsection_.css("p.related_news")
        related_news = related_news_.css("a::attr(href)").extract()

        listcontent = []
        listcontent_ = response.xpath('//article/p').extract()
        for i in range (len(listcontent_) - 1):
            sel = Selector(text=listcontent_[i])
            listcontent.append(sel.xpath('string(//p[1])').extract_first())

        # content = "".join(response.xpath('//article/p[@class="Normal"]/text()').extract())
        content = "".join(item for item in listcontent).strip()
        # author = subsection_.css("article strong::text").extract_first()
        try:
            author = subsection_.css("article strong::text")[-1].extract()
        except:
            author = response.xpath('//p[@class="author_mail"]/strong/text()').extract_first()
            # author = subsection_.css("article strong::text")[-1].extract()
        # filename = '%s.json' %page

        data = {
            'timestamp': timestamp,
            'title': title,
            'description': description,
            'related_news': related_news,
            'content': content,
            'author': author
        }
        yield data
