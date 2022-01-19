

import jieba
import math
from string import punctuation
from heapq import nlargest
from itertools import product, count
from gensim.models import word2vec
import numpy as np
# from keywords_moudle import get_corpus
# from keywords_moudle import read_excel
from textrank import TextRank
from get_corpus import Corpus
from read_excel import get_news
from ltp import LTP



news = get_news()
titles,contents = news.titles_texts()
stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
# tfidf = tf_idf()

corpus = cor.preprocess(contents)



for item in contents:
    tr = TextRank(item)
    for line in  tr.use():
        print(line)
    break