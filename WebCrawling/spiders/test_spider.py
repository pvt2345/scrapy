import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = [
            'https://kinhdoanh.vnexpress.net/tin-tuc/quoc-te/nha-may-my-thanh-nan-nhan-vi-don-thue-cua-ong-trump-3824309.html',
            # 'http://quotes.toscrape.com/page/2/',
        ]

    # def start_requests(self):
    #     urls = [
    #         'https://thethao.vnexpress.net/tin-tuc/bong-da-trong-nuoc/hlv-park-hang-seo-viet-nam-phai-dung-dau-bang-tai-aff-cup-3824068.html',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        body = response.css("body")[0]
        section = body.css("section.container")[0]
        subsection = section.css("section.wrap_sidebar_12")[0]
        subsection_ = subsection.css("section.sidebar_1")[0]
        filename = 'quotes-%s.html' % page
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(subsection_.extract())
        self.log('Saved file %s' % filename)