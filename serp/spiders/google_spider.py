import scrapy
from urllib import parse
import json
from bs4 import BeautifulSoup
from ..items import AutoCompleteItem, ResultItem, RelatedItem


def create_autocompelete_url(keyword):
    query_string = {'q': keyword, 'cp': 10, 'client': 'gws-wiz', 'xssi': 't',
              'gs_ri': 'gws-wiz', 'hl': 'fa', 'authuser': 0, 'pq': keyword, 'dpr': 1}
    autocomplete_url = 'https://www.google.com/complete/search?' + parse.urlencode(query_string)
    return autocomplete_url


class GoogleSpider(scrapy.Spider):
    name = 'google'

    def start_requests(self):
        # set number of results on the results page
        # The allowed values are 10, 20, 30, 40, 50, and 100.
        result_number = 10

        # input keywords you want to search here
        keywords = [
            # 'عسل',
        ]
        for keyword in keywords:
            query_string = {'q': keyword, 'num': result_number, 'client': 'ubuntu', 'gl': 'ir'}
            url = 'https://www.google.com/search?&' + parse.urlencode(query_string)
            # yield 2 types of urls for scraping
            # for the default result page
            yield scrapy.Request(url, callback=self.parse, cb_kwargs={'keyword': keyword})
            # for auto complete suggestions
            yield scrapy.Request(create_autocompelete_url(keyword), callback=self.parse,
                                 cb_kwargs={'keyword': keyword})

    def parse(self, response, keyword):
        # parse both types :
        # first auto complete content
        if 'complete/search' in response.url:
            # find auto complete suggestions
            for suggestion in json.loads(response.text[5:])[0]:
                item = AutoCompleteItem()
                item.fields["keyword"] = keyword
                item.fields["suggestion"] = suggestion[0]
                yield item
        else:
            soup = BeautifulSoup(response.body, 'html.parser')
            # find search results
            for i, result in enumerate(soup.find_all('div', 'yuRUbf')):
                item = ResultItem()
                item.fields["title"] = result.h3.get_text()
                item.fields["rank"] = i+1
                item.fields["link"] = result.a.get('href')
                item.fields["keyword"] = keyword
                yield item
            # find related searches
            for related in soup.find_all('a', 'k8XOCe'):
                related_keyword = related.find('div', 's75CSd').get_text()
                link = 'https://www.google.com' + related.get('href')
                item = RelatedItem()
                item.fields["keyword"] = keyword
                item.fields["related_keyword"] = related_keyword
                item.fields["link"] = link
                yield item
                # go for inner related keywords
                yield scrapy.Request(link, callback=self.parse, cb_kwargs={'keyword': related_keyword})
                yield scrapy.Request(create_autocompelete_url(related_keyword), callback=self.parse,
                                     cb_kwargs={'keyword': related_keyword})
