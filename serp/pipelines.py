# item pipelines
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .items import ResultItem, RelatedItem, AutoCompleteItem
from pandas import DataFrame
import logging


class ExcelExporter(object):
    def __init__(self):
        # 3 dicts for scraped items
        self.result = {'keyword': [], 'rank': [], 'title': [], 'link': []}
        self.related = {'keyword': [], 'related_keyword': [], 'link': []}
        self.suggestion = {'keyword': [], 'suggestion': []}

    def process_item(self, spider, item):
        # append the scraped items to their corresponding dicts
        if isinstance(spider, ResultItem):
            self.result['keyword'].append(spider.fields['keyword'])
            self.result['rank'].append(spider.fields['rank'])
            self.result['title'].append(spider.fields['title'])
            self.result['link'].append(spider.fields['link'])
        elif isinstance(spider, RelatedItem):
            self.related['keyword'].append(spider.fields['keyword'])
            self.related['related_keyword'].append(spider.fields['related_keyword'])
            self.related['link'].append(spider.fields['link'])
        elif isinstance(spider, AutoCompleteItem):
            self.suggestion['keyword'].append(spider.fields['keyword'])
            self.suggestion['suggestion'].append(spider.fields['suggestion'])
        return spider.fields

    def close_spider(self, spider):
        # create the files when crawling is completed
        # convert to data frames
        df1 = DataFrame({'keyword': self.result['keyword'],
                         'rank': self.result['rank'],
                         'title': self.result['title'],
                         'link': self.result['link']})
        df2 = DataFrame({'keyword': self.related['keyword'],
                         'title': self.related['related_keyword'],
                         'link': self.related['link']})
        df3 = DataFrame({'keyword': self.suggestion['keyword'],
                         'suggestion': self.suggestion['suggestion']})
        # create excel files
        df1.to_excel(f'results.xlsx', sheet_name='search results', index=False)
        df2.to_excel(f'related.xlsx', sheet_name='related searches', index=False)
        df3.to_excel(f'suggestion.xlsx', sheet_name='related searches', index=False)
        # message in log
        logging.info('3 excel files created successfully!')

