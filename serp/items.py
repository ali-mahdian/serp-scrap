# the models for scraped items
# documentation : https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutoCompleteItem(scrapy.Item):
    keyword = scrapy.Field()
    suggestion = scrapy.Field()


class ResultItem(scrapy.Item):
    keyword = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()


class RelatedItem(scrapy.Item):
    keyword = scrapy.Field()
    related_keyword = scrapy.Field()
    link = scrapy.Field()

