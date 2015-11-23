import scrapy
from items import LinkItem,DocItem
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
import json
import codecs
from BeautifulSoup import BeautifulSoup as BeautifulSoup
import ExtMainText 
import Html
class NewsSpider(CrawlSpider):
        name = "news"
        
        def __init__(self,query):
            self.start_urls = ["http://news.baidu.com/ns?rn=20&word=%s" % query]
            print self.start_urls

        def parse(self,response):
            item = LinkItem()
            soup = BeautifulSoup(response.body) 
            self.get_url(soup,item)
            #self.h = html2text.HTML2Text()
            #self.h.ignore_links = True
            if 'urls' in item:
                count = float(len(item['urls']))
                i = count+1
                for url in item['urls']:
                    i -= 1
                    yield Request(url=url, meta={'url':url,'weight':float(i/count),'item': item}, callback=self.parse_details)

        def parse_details(self,response):
            linkItem = response.meta['item']
            docItem = DocItem() 
            docItem['weight'] = response.meta['weight']
            docItem['url'] = response.meta['url']
            self.get_content(response,docItem) 
            self.get_title(response,docItem) 
            return docItem          

        def get_content(self,response,item):
            content = ExtMainText.GetContent(response.body,None,None)
            item['content'] = Html.filter_tags(content)
            #print h.handle(content)
            #print item['content'] 

        def get_title(self,response,item):
            title=response.xpath("/html/head/title/text()").extract()
            if title:
                # print 'title:'+title[0][:-5].encode('utf-8')
                item['title']=title[0].strip()

        def get_url(self,response,item):
            news_url=response.findAll('div',attrs={'id':True,'class':'result'})
            result = []
            for news in news_url:
                result.append(news.contents[0].contents[0]['href'])
            item['urls']=result
