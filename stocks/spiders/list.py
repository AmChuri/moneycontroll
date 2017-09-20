from __future__ import unicode_literals
import scrapy
# from stocks.items import StocksItem
from stocks.items import StocksItem


class StocksSpider(scrapy.Spider):
    name = "list"

    start_urls = ['http://www.moneycontrol.com/india/stockpricequote/A', ]

    def parse(self, response):
        item = StocksItem()
        for row in response.css(".pcq_tbl"):
            item['name'] = response.css('.pcq_tbl tr a::text').extract()
            item['url'] = response.css('.pcq_tbl tr a::attr(href)').extract()

            yield item