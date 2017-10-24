import scrapy
import sys
import importlib
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class SimpleSpider(scrapy.Spider):
    name = 'simple'

    def start_requests(self):
        core = getattr(self, 'core', None)
        if core is not None:
            self.core = importlib.import_module('cores.' + core)
            return [scrapy.Request(self.core.Page.start_url, self.parse)]
        else:
            return []

    def parse(self, response):
        page = self.core.Page(response)
        for o in page.output:
            yield o
        if page.has_next:
            yield scrapy.Request(page.next, self.parse)
