import scrapy

class Author_Spider(scrapy.Spider):
    name = 'Author'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('.author + a::attr(href)'): #select ra các thẻ có class = author và thẻ a ở trong đó
            yield response.follow(href, self.parse_author)

        # follow pagination links
        for href in response.css('li.next a::attr(href)'): #select ra thẻ li có class = next và thẻ a ở trong
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'placeofbirth': extract_with_css('.author-born-location::text')[3:],
            'bio': extract_with_css('.author-description::text'),
        }