# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from imdbproject2.items import Imdbproject2Item

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    # allowed_domains = ['example.com']
    start_urls = ['https://www.imdb.com/interfaces/']

    def parse(self, response):
        links = response.css('br+a::attr(href)').getall()[0]
        print(links)
        if links:
            new_link = response.urljoin(links)
            yield scrapy.Request(url = new_link, callback = self.parse_details)

    def parse_details(self, response):
        set_of_links = response.css('a::attr(href)').getall()
        set_of_links.pop(0)
        # for link in set_of_links:
        item = Imdbproject2Item()
        item['file_urls'] = set_of_links
        yield item
