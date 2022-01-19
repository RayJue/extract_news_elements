from signal import pthread_kill
from gensim.models import word2vec
from keywords_moudle.read_excel import get_news
from keywords_moudle.get_corpus import Corpus
from heapq import nlargest
from keywords_moudle.tfidf import tf_idf
from keywords_moudle.use_w2v import sim
from keysentence_moudle.textrank import TextRank
from keyinfo_extract_moudle.LTP_extract import Extract_elements
from keysentence_moudle.utils import use_expand,compute_similarity_by_avg

news = get_news()
titles,contents = news.titles_texts()
model = word2vec.Word2Vec.load('/home/rayjue/extract_news/news.model')

stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
get_sim = sim()
corpus,pec = cor.preprocess_st(contents)


tf = tf_idf()
ext = Extract_elements()
import heapq
from keysentence_moudle.judge import elements

for item in corpus:
    index = corpus.index(item)
    len_sent = len(contents[index])
    expand_title = use_expand(titles[index])
    sents = ''.join(item).split('。')
    _,stop_pec = cor.corpus_st(item,cor.getstopword())
    judge = elements(pec,len_sent,stop_pec,get_sim,tf)

    sim_with_title = judge.sim_with_title(expand_title,sents)
    ranked_sentence = judge.get_text_rank(sents)
    tfidf_sentence = judge.get_tfidf_rank(sents)

    sort1 = []
    sort2 = []
    for line in sents:
        line_index = sents.index(line)
        
        elements_1 = 0.1*len_sent+5*stop_pec+1*sim_with_title(titles[index],line)+100*ranked_sentence[line]

        elements_2 = 0.1*len_sent+5*stop_pec+1*sim_with_title(titles[index],line)+100*tfidf_sentence[line]

        sort1.append(elements_1)
        sort2.append(elements_2)
    
    print("textrank:"+'\t'.join(sort1))
    print("tdidf:"+'\t'.join(sort2))
    
    

    



    

    
    


    








