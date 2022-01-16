from signal import pthread_kill
import jieba
import math
from string import punctuation
from heapq import nlargest
from itertools import product, count
from gensim.models import word2vec
import numpy as np
from get_corpus import Corpus
from read_excel import get_news
from ltp import LTP


class sim:
    def __init__(self) -> None:
        self.model = word2vec.Word2Vec.load('/home/rayjue/extract_news/news.model')

    def compute_similarity_by_avg(self,sents_1, sents_2):
        # for sents_2 in sents_2s:
            vec1 = 0.0
            vec2 = 0.0
            if len(sents_1) == 0 or len(sents_2) == 0:
                return 0.0
        
            for word1 in sents_1:
                if word1 in self.mode:
                    vec1 = vec1 + self.mode[word1]
                else:
                    vec1 += self.mode['没有']
                
            for word2 in sents_2:
                if word2 in self.mode:
                    vec2 = vec2 + self.mode[word2]
                else:
                    vec2 += self.mode['没有']
            
                similarity = self.cosine_similarity(vec1 / len(sents_1), vec2 / len(sents_2))

            return similarity