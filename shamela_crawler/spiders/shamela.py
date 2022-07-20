from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ShamelaSpider(CrawlSpider):
    name = "shamela"
    allowed_domains = ["shamela.ws"]
    start_urls = ["https://shamela.ws/"]

    rules = (
        Rule(LinkExtractor(allow=r"category/"), callback="parse_item", follow=True),
    )

    def parse_item(self, response: Response):
        for book in response.css(".book_item"):
            yield {
                "title": book.css("a.book_title::text").get(),
                "author": book.css("a.text-gray::text").get(),
                "description": book.css("p.des::text").get().replace("\r", "\n"),
                "link": book.css("a.book_title::attr(href)").get(),
            }
