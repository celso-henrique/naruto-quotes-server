# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy.utils import response
from collections import OrderedDict

class NarutoquotesSpider(scrapy.Spider):
    name = 'narutoQuotes'
    allowed_domains = ['www.less-real.com']
    start_urls = ['https://www.less-real.com/quotes/search/Naruto']
    def parse(self, response):
        pass
        quotes = response.css('div.quote').css('span.quoteText::text').extract()
        speakers = response.css('div.quote').css('a::text').extract()
        element = speakers[1]
        newspeakers =[]
        for i in speakers:
            if i != element:
                newspeakers.append(i)
        speakers = newspeakers
        full = [speakers,quotes]
        df = pd.DataFrame(full)
        df.to_csv('Data/narutoQuos.csv',mode='a')
        for i in range(len(speakers)):
            item = {
                'Speakers' : speakers[i],
                'Quotes':  quotes[i]
            }
            yield item
        nexturl = response.css('a#next::attr(href)').extract_first()
        if nexturl:
            nexturl = response.urljoin(nexturl)
            yield scrapy.Request(url = nexturl,callback = self.parse)