# -*- coding: utf-8 -*-
 
 
from gensim.models import word2vec
from read_excel import get_news
from get_corpus import Corpus
from tfidf import tf_idf
# import jieba

news = get_news()
titles,contents = news.titles_texts()

stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
tfidf = tf_idf()

cor.write_corpus(contents)
 
sentences = word2vec.Text8Corpus(r'/home/rayjue/extract_news/corpus.txt')
 
model = word2vec.Word2Vec(sentences, size=100, hs=1, min_count=1, window=3)
 
model.save(u'/home/rayjue/extract_news/news.model/news.model')