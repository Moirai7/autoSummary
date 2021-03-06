import TextRank4Sentence

class RelatedDocs(object):
    def GetDocs(self, items,threshold=1.0):
        tr4s = TextRank4Sentence.TextRank4Sentence(stop_words_file='abstract/stopword.txt')
        docs = items
        lens = len(docs)
        result = [[] for i in range(lens)]
        i = 0
        for x in xrange(lens):
            if 'category' in docs[x]:
                continue
            for k  in xrange(lens):
                if x == k:
                    continue
                if 'category' in docs[k]:
                    if tr4s.GetSentenceSim(docs[x]['title'],docs[k]['title'])>threshold:
                        result[docs[k]['category']].append(docs[x])
                        docs[x]['category'] = docs[k]['category']
                        break      
            if 'category' not in docs[x]:
                result[i].append(docs[x])
                docs[x]['category'] = i
                i+=1
        return result
