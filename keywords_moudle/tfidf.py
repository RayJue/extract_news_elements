import os
import codecs
import math
import operator


class tf_idf:
    def __init__(self) -> None:
        pass





    def freqword(self,wordlis):  # 统计词频，并返回字典
        freword = {}
        for i in wordlis:
            if str(i) in freword:
                count = freword[str(i)]
                freword[str(i)] = count+1
            else:
                freword[str(i)] = 1
        return freword


    

    def wordinfilecount(self,word, corpuslist):  # 查出包含该词的文档数
        count = 0  # 计数器
        for i in corpuslist:
            for j in i:
                if word in set(j):  # 只要文档出现该词，这计数器加1，所以这里用集合
                    count = count+1
                else:
                    continue
        return count


    def tf_idf(self,wordlis, len_filelist, corpuslist):  # 计算TF-IDF,并返回字典
        outdic = {}
        tf = 0
        idf = 0
        dic = self.freqword(wordlis)
        outlis = []
        for i in set(wordlis):
            tf = dic[str(i)]/len(wordlis)  # 计算TF：某个词在文章中出现的次数/文章总词数
            # 计算IDF：log(语料库的文档总数/(包含该词的文档数+1))
            idf = math.log(len_filelist/(self.wordinfilecount(str(i), corpuslist)+1))
            tfidf = tf*idf  # 计算TF-IDF
            outdic[str(i)] = tfidf
        orderdic = sorted(outdic.items(), key=operator.itemgetter(
            1), reverse=True)  # 给字典排序
        return orderdic
