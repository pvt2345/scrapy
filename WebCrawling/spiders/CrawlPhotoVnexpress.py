import scrapy
# from scrapy.spiders import CrawlSpider
from scrapy import Selector

class PhotoCrawl(scrapy.Spider):
    name = 'photo_crawler'
    start_urls = ['https://vnexpress.net/photo/tu-lieu/cac-cong-trinh-ha-tang-dang-cap-quoc-te-cua-malaysia-3851977.html',
                  'https://vnexpress.net/photo/nguoi-viet-5-chau/le-vieng-chu-tich-nuoc-tran-dai-quang-tai-cac-nuoc-3815256.html']

    def parse(self, response):
        main = response.css("section.container").css("section.sidebar_1")
        timestamp = main.css("header").css("span::text").extract_first()
        title = main.css("h1::text").extract_first().strip()
        description = main.css("h2::text").extract_first().strip()
        related_news = main.css("p.related_news").css("a::attr(href)").extract()
        # photo = main.css("div.item_slide_show").css('img[class*=displayAfterResize]::attr(data-original)').extract()
        photo_set = main.css("div.item_slide_show").extract()
        photo = []
        for item in photo_set:
            # photo_link = item.css('img[class*=displayAfterResize]::attr(data-original)').extract_first()
            sel = Selector(text=item)
            photo_link = sel.css('img[class*=displayAfterResize]::attr(data-original)').extract_first()
            # listcontent.append(sel.xpath('string(//p[1])').extract_first())
            # caption = "".join(sel.css('div.desc_cation').css('p::text').extract())
            caption = "".join(sel.xpath("//p//text()").extract())
            if(caption is not None):
                photo.append({"photo_link" : photo_link, "caption" : caption})
            else:
                photo.append({"photo_link" : photo_link})

        data = {
            "timestamp" : timestamp,
            "title" : title,
            "description" : description,
            "related_news" : related_news,
            "photo" : photo
        }

        yield data
