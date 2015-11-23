from items import SentenceItem,ParagraphItem
from Segmentation import SentenceSegmentation

class StructuralDocs(object):
    def __init__(self):
        self.seg = SentenceSegmentation()

    def __deleteSentence(self,sentence):
        if len(sentence)<8 or (sentence.find(u'\u4e0a\u4e00\u9875')!=-1) or (sentence.find(u'\u4e0b\u4e00\u9875')!=-1) or (sentence.find(u'\u884c\u4e1a\u52a8\u6001')!=-1) or (sentence.find(u'\u5173\u952e\u8bcd')!=-1) or (sentence.find(u'\u5ef6\u4f38\u9605\u8bfb')!=-1) or (sentence.find(u'\u6765\u6e90')!=-1)  or (sentence.find(u'\u5b57\u53f7')!=-1)  or (sentence.find(u'\u8d23\u4efb\u7f16\u8f91')!=-1) or (sentence.find(u'\u4e3e\u62a5')!=-1)or (sentence.find(u'\u4eac\u7f51\u6587')!=-1)or (sentence.find(u'\u76d1\u7763\u7535\u8bdd')!=-1) or (sentence.find(u'\u7248\u6743')!=-1) or (sentence.find(u'\u90ae\u7f16')!=-1)or (sentence.find(u'\u65b0\u6d6a\u7f51')!=-1) or (sentence.find(u'\u7f51\u8baf')!=-1) or (sentence.find(u'\u514d\u8d23\u58f0\u660e')!=-1):
            return False
        return True
    def GetDocsStruct(self, items):
        docs = items
        #import pdb
        for doc in docs:
            paragraph = doc['content'].split('\n')
            lens = len(paragraph)
            doc['paragraphs'] = []
            for x in xrange(lens):
                p = ParagraphItem()
                p['weight'] = float(lens-x)/lens
                p['content'] = paragraph[x]
                p['sentences']=[]
                sentences = self.seg.segment(p['content'])

                lens_s = len(sentences)
                for y in xrange(lens_s):
                    if self.__deleteSentence(sentences[y]):
                        s = SentenceItem()
                        s['weight'] = float(lens_s-y)/lens_s*p['weight']
                        s['content'] = sentences[y]
                        p['sentences'].append(s)
                doc['paragraphs'].append(p)
            #print doc
            #pdb.set_trace()
        print 'end'
        return docs
        
