import imp
import re
from signal import pthread_kill
from gensim.models import word2vec
from keywords_moudle.read_excel import get_news
from keywords_moudle.get_corpus import Corpus
from heapq import nlargest
from itertools import product, count
from keywords_moudle.tfidf import tf_idf
from keywords_moudle.use_w2v import sim
from keysentence_moudle.textrank import TextRank
from keyinfo_extract_moudle.LTP_extract import Extract_elements
# from read_excel import get_news
import jieba
from utils import cosine_similarity

# from tfidf import tf_idf
news = get_news()
titles,contents = news.titles_texts()
model = word2vec.Word2Vec.load('/home/rayjue/extract_news/news.model')

stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
# tfidf = tf_idf()


get_sim = sim()


corpus,pec = cor.preprocess_st(contents)



class elements(object):
    def __init__(self,get_sim,tf) -> None:
        super().__init__()
        self.tf = tf
        self.get_sim = get_sim
        



    def sim_with_title(self,expand_title,sents):

        return get_sim.compute_similarity_by_avg(expand_title,sents)
    
    def get_text_rank(self,sents):
            select = {}
        
            tr = TextRank(sents)
            for line in  tr.use():
                select[line[0]] = line[1]
        
            return select


    def get_tfidf_rank(self,sents,contents,corpus):

        
        _,avg =  self.tf.tf_idf_sf(sents, len(contents),corpus)

        res = {sents.index(i):j for i,j in _}

        return res

    # def get_elem_1(self,sents,corps):
    #     return 0.1*self.len_sent+5*self.stop_pec+1*self.sim_with_title(titles[index],line)+100*self.ranked_sentence[line]

    # def get_elem_2(self,sents,corps):
    #     return 0.1*self.len_sent+5*self.stop_pec+1*self.sim_with_title(titles[index],line)+100*tfidf_sentence[line]






