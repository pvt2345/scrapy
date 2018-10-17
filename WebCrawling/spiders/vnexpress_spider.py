import scrapy
import json
import codecs

class VnexpressSpider(scrapy.Spider):
    name = "vnexpress"
    start_urls = [
           'https://thethao.vnexpress.net/tin-tuc/cac-giai-khac/phap-day-duc-den-mieng-vuc-xuong-hang-o-nations-league-3825111.html',
           'https://thethao.vnexpress.net/tin-tuc/cac-giai-khac/ha-lan-thang-dam-duc-o-nations-league-3823679.html?cvar=A'
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
        content = " ".join(subsection_.css("article p::text").extract())
        author = subsection_.css("article strong::text").extract_first()

        filename = '%s.json' %page

        data = {
            'timestamp': timestamp,
            'title': title,
            'description': description,
            'related_news': related_news,
            'content': content,
            'author': author
        }

        with codecs.open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)


        # filename = 'quotes-%s.html' % page
        # with open(filename, 'w', encoding='UTF-8') as f:
        #     f.write(subsection_.extract())
        # self.log('Saved file %s' % filename)