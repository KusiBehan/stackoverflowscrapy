from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]
    def parse(self, response):
        questions = Selector(response).xpath('//*[@id="questions"]/div/div[2]/h3')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="s-link"]/text()').extract_first()
            item['url'] = "https://stackoverflow.com" + question.xpath(
                'a[@class="s-link"]/@href').extract_first()
            yield item
