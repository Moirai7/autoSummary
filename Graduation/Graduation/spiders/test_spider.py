import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
import json
import codecs
from BeautifulSoup import BeautifulSoup as BeautifulSoup
import ExtMainText 
import Html

file = open('t.t','wb')
class TestSpider(CrawlSpider):
    #filename = codecs.open('tencent_data.json', mode='wb', encoding='utf-8')
    name = "test"
    allowed_domains = ["bbs.tianya.cn"]

    start_urls =["http://bbs.tianya.cn/post-free-2052991-1.shtml"]


    def parse(self,response):
            content = ExtMainText.GetContent(response.body,None,None)
            print content
            file.write(content)
