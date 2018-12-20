import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy import Selector
from WebCrawling.items import File_Item

class FileCrawler(CrawlSpider):
    name = 'file_crawler'
    allowed_domains = ['k1.caict.ac.cn']
    start_urls = []
    for i in range(10, 19):
        for j in range(1, 13):
            if (j/10 == 0): #1->9
                start_urls.append('http://k1.caict.ac.cn/yjts/qqzkgz/zksl/' + '20{}'.format(i) + '0{}/'.format(j))
            else:
                start_urls.append('http://k1.caict.ac.cn/yjts/qqzkgz/zksl/' + '20{}'.format(i) + '{}/'.format(j))
    # start_urls = ['http://k1.caict.ac.cn/yjts/qqzkgz/zksl/201702/']
                  # 'http://k1.caict.ac.cn/yjts/qqzkgz/zksl/201[0-18][10-12]/']

    # def parse(self, response):
    #     for href in response.css("a::attr(href)")[1:].extract():
    #         yield Request(url=response.urljoin(href), callback=self.parse_file)
    #     # yield data
    # def parse_file(self, response):
    #     path = 'D:/File/' + response.url.split('/')[-2] + response.url.split('/')[-1]
    #     print(response.url.split('/')[-1])
    #     with open(path, 'wb') as f:
    #         f.write(response.body)
    def parse(self, response):
        file_urls = []
        for href in response.css("a::attr(href)")[1:].extract():
            # yield Request(url=response.urljoin(href)
            file_urls.append(response.urljoin(href))
            print(response.urljoin(href))
        yield File_Item(
            # file_urls = ['http://k1.caict.ac.cn/yjts/qqzkgz/zksl/201702/P020170217521456624143.pdf']
            file_urls = file_urls
        )