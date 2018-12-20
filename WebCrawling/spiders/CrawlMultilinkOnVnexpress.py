from scrapy.spiders import CrawlSpider, Rule
from scrapy import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector

class VnexpressSpider(CrawlSpider):
    name = 'multilink_spider_vnexpress'
    # allowed_domains = ['vnexpress.net', 'kinhdoanh.vnexpress.net', 'thethao.vnexpress.net', 'giaitri.vnexpress.net', 'suckhoe.vnexpress.net', 'doisong.vnexpress.net', 'dulich.vnexpress.net', 'sohoa.vnexpress.net']
    # start_urls = ['https://vnexpress.net/tin-tuc/the-gioi']
    # rules = (
    #     Rule(LinkExtractor(allow='https://vnexpress.net/tin-tuc/the-gioi/page/[1-5].html')),
    #     Rule(LinkExtractor(allow=('/the-gioi/[0-9A-Za-z-]*.html'), deny=(
    #         'https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/photo/', '/infographics/'), ),
    #          callback='parse_item'),
    # )
    def __init__(self, category='the-gioi', pages = '1'):
        super(VnexpressSpider, self).__init__()
        if(category in ['the-gioi', 'thoi-su', 'phap-luat', 'giao-duc', 'khoa-hoc', 'oto-xe-may', 'cong-dong', 'tam-su']):
            self.allowed_domains = ['vnexpress.net']
            self.start_urls = ['https://vnexpress.net/tin-tuc/%s' %category]
            self.rules = (
            Rule(LinkExtractor(allow='https://vnexpress.net/tin-tuc/{}/page/[1-{}].html'.format(category, pages))),
            Rule(LinkExtractor(allow=('/%s/[0-9A-Za-z-]*.html' %category), deny=('https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/infographics/'),),
                                        callback='parse_item'),
            Rule(LinkExtractor(allow=('/photo/')), callback='parse_photo')
            )


        elif(category == 'kinh-doanh'):
            self.allowed_domains = ['kinhdoanh.vnexpress.net']
            self.start_urls = ['https://kinhdoanh.vnexpress.net/']
            self.rules = (
                    Rule(LinkExtractor(allow='https://kinhdoanh.vnexpress.net/page/[1-%s].html' %pages)),
                # Rule(LinkExtractor(allow=('/tin-tuc/[0-9A-Za-z]*.html',
                #                           '/tin-tuc/doanh-nghiep/[0-9A-Za-z-]*.html', '/tin-tuc/doanh-nghiep/doanh-nghiep-viet/[0-9A-Za-z-]*.html', #doanh_nghiep
                #                           '/tin-tuc/bat-dong-san/[0-9A-Za-z-]*.html', '/tin-tuc/bat-dong-san/du-an/[0-9A-Za-z-]*.html', #bat dong san
                #                           '/tin-tuc/ebank/[0-9A-Za-z-]*.html', '/tin-tuc/ebank/ngan-hang/[0-9A-Za-z-]*.html', '/tin-tuc/ebank/thanh-toan-dien-tu/[0-9A-Za-z-]*.html', '/tin-tuc/ebank/tuyen-dung/[0-9A-Za-z-]*.html', '/tin-tuc/ebank/cong-dong/[0-9A-Za-z-]*.html', 'tin-tuc/ebank/tu-van/[0-9A-Za-z-]*.html', #ebank
                #                           '/tin-tuc/thuong-mai-dien-tu/[0-9A-Za-z-]*.html', ''
                #                           '/tin-tuc/quoc-te/phan-tich/[0-9A-Za-z-]*.html', '/tin-tuc/quoc-te/[0-9A-Za-z-]*.html',),
                #                    deny=('https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/photo/', '/infographics/'), ),
                #                    callback='parse_item'),
                Rule(LinkExtractor(allow=('/tin-tuc/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[a-z-]*/[0-9A-Za-z-]*.html',),
                                     deny=('https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/photo/', '/infographics/')),
                                     callback='parse_item'),
            )

        elif (category == 'giai-tri'):
            self.allowed_domains = ['giaitri.vnexpress.net']
            self.start_urls = ['https://giaitri.vnexpress.net/']
            self.rules = (
                Rule(LinkExtractor(allow='https://giaitri.vnexpress.net/page/[1-%s].html' % pages)),
                Rule(LinkExtractor(allow=('/tin-tuc/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[a-z-]*/[0-9A-Za-z-]*.html',),
                                   deny=('https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/photo/',
                                         '/infographics/')),
                     callback='parse_item'),
            )

        elif (category == 'the-thao'):
            self.allowed_domains = ['thethao.vnexpress.net']
            self.start_urls = ['https://thethao.vnexpress.net/']
            self.rules = (
                Rule(LinkExtractor(allow='https://thethao.vnexpress.net/page/[1-%s].html' % pages)),
                Rule(LinkExtractor(allow=('/tin-tuc/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[a-z]*/[0-9A-Za-z-]*.html',
                                          '/tuong-thuat/[0-9A-Za-z-]*.html',
                                          ),
                                   deny=('https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/photo/',
                                         '/infographics/')),
                     callback='parse_item'),
            )

        elif (category == 'suc-khoe'):
            self.allowed_domains = ['suckhoe.vnexpress.net']
            self.start_urls = ['https://suckhoe.vnexpress.net/']
            self.rules = (
                Rule(LinkExtractor(allow='https://suckhoe.vnexpress.net/page/[1-%s].html' % pages)),
                Rule(LinkExtractor(allow=('/tin-tuc/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[a-z-]*/[0-9A-Za-z-]*.html',),
                                   deny=('https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/photo/',
                                         '/infographics/')),
                     callback='parse_item'),
            )

        elif (category == 'doi-song'):
            self.allowed_domains = ['doisong.vnexpress.net']
            self.start_urls = ['https://doisong.vnexpress.net/']
            self.rules = (
                Rule(LinkExtractor(allow='https://doisong.vnexpress.net/page/[1-%s].html' % pages)),
                Rule(LinkExtractor(allow=('/tin-tuc/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[a-z-]*/[0-9A-Za-z-]*.html',),
                                   deny=('https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/photo/',
                                         '/infographics/')),
                     callback='parse_item'),
            )

        elif (category == 'du-lich'):
            self.allowed_domains = ['dulich.vnexpress.net']
            self.start_urls = ['https://dulich.vnexpress.net/']
            self.rules = (
                Rule(LinkExtractor(allow='https://dulich.vnexpress.net/page/[1-%s].html' % pages)),
                Rule(LinkExtractor(allow=('/tin-tuc/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[a-z-]*/[0-9A-Za-z-]*.html',),
                                   deny=('https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/photo/',
                                         '/infographics/')),
                     callback='parse_item'),
            )

        elif (category == 'so-hoa'):
            self.allowed_domains = ['sohoa.vnexpress.net']
            self.start_urls = ['https://sohoa.vnexpress.net/']
            self.rules = (
                Rule(LinkExtractor(allow='https://sohoa.vnexpress.net/page/[1-%s].html' % pages)),
                Rule(LinkExtractor(allow=('/tin-tuc/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[0-9A-Za-z-]*.html',
                                          '/tin-tuc/[a-z-]*/[a-z-]*/[0-9A-Za-z-]*.html',),
                                   deny=('https://video.vnexpress.net/tin-tuc/the-gioi/[0-9A-Za-z-]*.html', '/photo/',
                                         '/infographics/')),
                     callback='parse_item'),
            )
        self._compile_rules()

    def parse_item(self, response):
        try:
            # page = response.url.split("/")[-1]
            # page = page.split(".")[0]
            body = response.css("body")[0]
            section = body.css("section.container")[0]
            subsection = section.css("section.wrap_sidebar_12")[0]
            subsection_ = subsection.css("section.sidebar_1")[0]
            timestamp = subsection_.css("header.clearfix span::text").extract_first()
            title = subsection_.css("h1::text").extract_first().strip()
            description = subsection_.css("h2::text").extract_first().strip()
            related_news_ = subsection_.css("p.related_news")
            related_news = related_news_.css("a::attr(href)").extract()

            listcontent = []
            listcontent_ = response.xpath('//article/p').extract()
            for i in range(len(listcontent_) - 1):
                sel = Selector(text=listcontent_[i])
                listcontent.append(sel.xpath('string(//p[1])').extract_first())

            # content = "".join(response.xpath('//article/p[@class="Normal"]/text()').extract())
            content = "".join(item for item in listcontent).strip()
            # author = subsection_.css("article strong::text").extract_first()
            try:
                author = subsection_.css("article strong::text")[-1].extract()
            except:
                author = response.xpath('//p[@class="author_mail"]/strong/text()').extract_first()
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

        except:
            main = response.css('section')[3].css('div.section_container')[1].css('div.width_common')[1].css('div.left')[0].css('div.width_common').xpath('//div[@id = "box_details_news"]')[0]
            # main = response.css('section')[3].xpath("//div[@id='box_details_news']")
            timestamp = main.css('header')[0].css('span::text').extract_first()
            title = main.css("div.title_news")[0].css("h1::text").extract_first()
            summary = main.css('h2::text').extract_first()
            related_news = main.css("div.relative_new ul li a::attr(href)").extract()
            listcontent = main.css("p::text").extract()[:-1]
            content = ''.join(item for item in listcontent)
            author = main.css("p strong::text")[-1].extract()

            a = {
                "timestamp": timestamp,
                "title": title,
                "summary": summary,
                "related_news": related_news,
                "content": content,
                "author": author
            }

            yield a

        finally:
            pass

    def parse_photo(self, response):
        main = response.css("section.container").css("section.sidebar_1")
        timestamp = main.css("header").css("span::text").extract_first()
        title = main.css("h1::text").extract_first().strip()
        description = main.css("h2::text").extract_first().strip()
        related_news = main.css("p.related_news").css("a::attr(href)").extract()
        # photo = main.css("div.item_slide_show").css('img[class*=displayAfterResize]::attr(data-original)').extract()
        photo_set = main.css("div.item_slide_show")
        photo = []
        for item in photo_set:
            photo_link = item.css('img[class*=displayAfterResize]::attr(data-original)').extract_first()
            caption = "".join(item.css('div.desc_cation').css('p::text').extract())
            if (caption is not None):
                photo.append({"photo_link": photo_link, "caption": caption})
            else:
                photo.append({"photo_link": photo_link})

        data = {
            "timestamp": timestamp,
            "title": title,
            "description": description,
            "related_news": related_news,
            "photo": photo
        }

        yield data
# if __name__ == '__main__':
#     VnexpressSpider()