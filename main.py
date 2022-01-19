import imp
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
from keysentence_moudle.judge import elements
from keysentence_moudle.utils import use_expand,compute_similarity_by_avg
from keyinfo_extract_moudle.analysis import LTP_Analysis
import jieba
from ltp import LTP
from utils import cosine_similarity
ltp = LTP()
nlp = LTP_Analysis()
news = get_news()
titles,contents = news.titles_texts()
model = word2vec.Word2Vec.load('/home/rayjue/extract_news/news.model')
stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
get_sim = sim()
corpus,pec = cor.preprocess_st(contents)
tf = tf_idf()
ext = Extract_elements(nlp,ltp)
element = elements(get_sim,tf)
import heapq
for item in corpus:
    index = corpus.index(item)
    len_sent = len(contents[index])
    expand_title = use_expand(model,titles[index])
    sents = ''.join(item).split('。')
    _,stop_pec = cor.corpus_st(item,cor.getstopword())

    ranked_sentence = element.get_text_rank(''.join(item))
    tfidf_sentence = element.get_tfidf_rank(sents,contents,corpus)

    sort1 = []
    sort2 = []
    for line in sents:
        line_index = sents.index(line)
        
        elements_1 = 0.1*len_sent+5*stop_pec[line_index]+1*element.sim_with_title(titles[index],line)+100*ranked_sentence[line_index]
        elements_2 = 0.1*len_sent+5*stop_pec[line_index]+1*element.sim_with_title(titles[index],line)+100*tfidf_sentence[line_index]

        sort1.append(elements_1)
        sort2.append(elements_2)
    
    for a in map(sort1.index, heapq.nlargest(3, sort1)):
        print("textrank:"+sents[a])
        print(ext.cal_elements(sents[a]))
    
    for a in map(sort2.index, heapq.nlargest(3, sort2)):
        print("tfidf:"+sents[a])
        print(ext.cal_elements(sents[a]))
    break
