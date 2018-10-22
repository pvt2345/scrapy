import scrapy
import json
import codecs
from scrapy import Selector

class VnexpressSpider(scrapy.Spider):
    name = "vnexpress"
    start_urls = [
                'https://vnexpress.net/tin-tuc/thoi-su/giao-thong/nguoi-dan-ba-lai-bmw-tong-gan-chuc-xe-may-o-sai-gon-3827260.html'
        ]

    # def start_requests(self):
    #     urls = [
    #         'https://thethao.vnexpress.net/tin-tuc/bong-da-trong-nuoc/hlv-park-hang-seo-viet-nam-phai-dung-dau-bang-tai-aff-cup-3824068.html',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        page = page.split(".")[0]
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
        content = "".join(item for item in listcontent)
        author = subsection_.css("article strong::text").extract_first()

        filename = '%s.txt' %page

        data = {
            'timestamp': timestamp,
            'title': title,
            'description': description,
            'related_news': related_news,
            'content': content,
            'author': author
        }
        with open(filename, "w", encoding='UTF-8') as f:
            f.write(content)

        f.close()
        yield data
