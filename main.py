import imp
from signal import pthread_kill
from gensim.models import word2vec
from keywords_moudle.read_excel import get_news
from keywords_moudle.get_corpus import Corpus
from heapq import nlargest
from itertools import product, count
from keywords_moudle.tfidf import tf_idf
from keywords_moudle.use_w2v import sim
from keysentence_moudle.textrank_extract import comparion,textrank_sort
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

compare = comparion()
textrank = textrank_sort()
get_sim = sim()


corpus,pec = cor.preprocess_st(contents)


def use_expand(title_):
    expand_title = []
    title = jieba.lcut(title_)
    for i in title:
        try:
            expand_title.append(i)
            sim = model.most_similar(i, topn=2)
            for key in sim:
                expand_title.append(key[0])
        except:
            print(' 训练语料未发现该词语')
            expand_title = title
    return expand_title

def compute_similarity_by_avg(sents_1, sents_2):

        vec1 = 0.0
        vec2 = 0.0
        if len(sents_1) == 0 or len(sents_2) == 0:
            return 0.0
       
        for word1 in sents_1:
            if word1 in model:
                vec1 = vec1 + model[word1]
            else:
                vec1 += model['没有']
            
        for word2 in sents_2:
            if word2 in model:
                vec2 = vec2 + model[word2]
            else:
                vec2 += model['没有']
        
            similarity = cosine_similarity(vec1 / len(sents_1), vec2 / len(sents_2))

        return similarity
tf = tf_idf()
ext = Extract_elements()
import heapq
for item in corpus:
    index = corpus.index(item)
    len_sent = contents[index]
    expand_title = use_expand(titles[index])
    sents = textrank.filter_model(item.split('。'))
    _,stop_pec = cor.corpus_st(sents,cor.getstopword())

    def sim_with_title(expand_title,sents):

        return get_sim.compute_similarity_by_avg(expand_title,sents)

    

    def get_text_rank(sents):
        graph = compare.create_graph(sents)

        scores = textrank.weight_sentences_rank(graph)
        sent_selected = nlargest(len(sents), zip(scores, count()))
        sent_index = []
        for i in range(5):
                sent_index.append(sent_selected[i])
                print(sent_selected[i])
        return {sents[i[1]]:sents[i[0]] for i in sent_index}
    ranked_sentence = get_text_rank(sents)

    def get_tfidf_rank(sents):

        
        _,avg =  tf.tf_idf_sf(sents, len(contents),corpus)

        return avg

    tfidf_sentence = get_text_rank(sents)




    sort1 = []
    sort2 = []
    for line in sents:
        line_index = item.index(line)

        elements_1 = 0.1*len_sent,0.5*stop_pec,1*sim_with_title(line,titles[index]),1*ranked_sentence[line]

        elements_2 = 0.1*len_sent,0.5*stop_pec,1*sim_with_title(line,titles[index]),1*tfidf_sentence[line]

        sort1.append(elements_1)
        sort2.append(elements_2)
    
    for a in map(sort1.index, heapq.nlargest(3, sort1)):
        print("textrank:"+sents[a])
        print(ext.cal_elements(sents[a]))
    
    for a in map(sort2.index, heapq.nlargest(3, sort2)):
        print("avg-tfidf"+sents[a])
        print(ext.cal_elements(sents[a]))

    



    

    
    


    








