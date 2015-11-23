from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess,Crawler
from scrapy.settings import Settings
from scrapy.xlib.pydispatch import dispatcher
from multiprocessing.queues import Queue
from multiprocessing import Process
from spiders.news_spider import NewsSpider
import abstract.RelatedDocs as rds
import abstract.StructuralDocs as sds
import abstract.TextRank4Sentence as tr

class CrawlerWorker(Process):
    def __init__(self, spider,query,results):
        Process.__init__(self)
        self.results = results
        self.items = []
        self.query = query
        self.spider = spider
        dispatcher.connect(self._item_passed, signals.item_passed)

    def _item_passed(self, item):
        self.items.append(item)

    def run(self):
        #self.crawler = CrawlerProcess(get_project_settings())
        self.crawler = CrawlerProcess(Settings())
        self.crawler.crawl(self.spider,self.query)
        self.crawler.start()
        self.crawler.stop()
        self.results.put(self.items)

def RunSpider(query):
    results = Queue()
    crawler = CrawlerWorker(NewsSpider(''),query, results)
    crawler.start()
    return results.get()

if __name__ == '__main__':
    results = Queue()
    crawler = CrawlerWorker(NewsSpider(''),'%D3%C5%D2%C2%BF%E2', results)
    crawler.start()
    docs = sds.StructuralDocs().GetDocsStruct(results.get())
    docs = rds.RelatedDocs().GetDocs(docs)
    tr4s = tr.TextRank4Sentence(stop_words_file='abstract/stopword.txt')
    for doc_simi in docs:
        abstracts = u''
        for doc in doc_simi:
            print doc['title']
            tr4s.train_weight(doc=doc)
            (sentence,weight) = tr4s.get_key_sentences(num=4)
            abstracts+=u'\u3002'.join(sentence)
        tr4s.Clear()
        tr4s.train(text=abstracts, speech_tag_filter=True, lower=True, source = 'all_filters')
        (sentence,weight) = tr4s.get_key_sentences(num=4)
        print u'\u3002'.join(sentence)
        print '\n\n'

