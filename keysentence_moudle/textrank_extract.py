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



news = get_news()
titles,contents = news.titles_texts()
stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
# tfidf = tf_idf()

corpus = cor.preprocess(contents)

#载入词向量
model = word2vec.Word2Vec.load('/home/rayjue/extract_news/news.model')


class comparion:
    def __init__(self) -> None:
        pass

    def two_sentences_similarity(self,sents_1, sents_2):
        counter = 0
        for sent in sents_1:
            if sent in sents_2:
                counter += 1
        return counter / (math.log(len(sents_1) + len(sents_2)))
    
    #余弦相似度
    def cosine_similarity(self,vec1, vec2):
        tx = np.array(vec1)
        ty = np.array(vec2)
        cos1 = np.sum(tx * ty)
        cos21 = np.sqrt(sum(tx ** 2))
        # print(ty)
        cos22 = np.sqrt(sum(ty ** 2))
        cosine_value = cos1 / float(cos21 * cos22)
        return cosine_value
    
    #求两句子平均词向量
    def compute_similarity_by_avg(self,sents_1, sents_2):

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
        
            similarity = self.cosine_similarity(vec1 / len(sents_1), vec2 / len(sents_2))

        return similarity
    
     
    def create_graph(self,word_sent):
        """
        传入句子链表  返回句子之间相似度的图
        :param word_sent:
        :return:
        """
        num = len(word_sent)
        board = [[0.0 for _ in range(num)] for _ in range(num)]
    
        for i, j in product(range(num), repeat=2):
            # print(i,j)
            if i != j:
                
                board[i][j] = self.compute_similarity_by_avg(word_sent[i], word_sent[j])
                # print(board)
            # else:
            #     break
        return board


class textrank_sort:

    def __init__(self) -> None:
        pass
    
    #计算句子在图中的分数
    def calculate_score(self,weight_graph, scores, i):
        length = len(weight_graph)
        d = 0.85
        added_score = 0.0
    
        for j in range(length):
            fraction = 0.0
            denominator = 0.0
            # 计算分子
            fraction = weight_graph[j][i] * scores[j]
            # 计算分母
            for k in range(length):
                denominator += weight_graph[j][k]
                if denominator == 0:
                    denominator = 1
            added_score += fraction / denominator
        # 算出最终的分数
        weighted_score = (1 - d) + d * added_score
        return weighted_score
 
    #输入相似度的图（矩阵),并返回各个句子的分数
    def weight_sentences_rank(self,weight_graph):
        # 初始分数设置为0.5
        scores = [0.5 for _ in range(len(weight_graph))]
        old_scores = [0.0 for _ in range(len(weight_graph))]
    
        # 开始迭代
        while self.different(scores, old_scores):

            for i in range(len(weight_graph)):
                # print(scores[i])
                old_scores[i] = scores[i]
            for i in range(len(weight_graph)):
                scores[i] = self.calculate_score(weight_graph, scores, i)
        return scores
 
    #判断前后分数有无变化
    def different(self,scores, old_scores):
        flag = False
        for i in range(len(scores)):
            if math.fabs(scores[i] - old_scores[i]) >= 0.0001:
                flag = True
                break
        return flag
    
    #过滤不在模型里的词语
    def filter_model(self,sents):
        _sents = []
        # print(sents)
        for sentence in sents:
            for word in sentence:
                if word not in model:
                    sentence.remove(word)
            if sentence:
                _sents.append(sentence)
        return _sents

    def filter_model(self,sents):
        _sents = []
        # print(sents)
        for sentence in sents:
            for word in sentence:
                if word not in model:
                    sentence.remove(word)
            if sentence:
                _sents.append(sentence)
        return _sents

compare = comparion()
textrank = textrank_sort()
sents = textrank.filter_model(corpus)
for text in sents:
    # print(sents.index(text))

    graph = compare.create_graph(contents[sents.index(text)])
    print(len(graph))
    scores = textrank.weight_sentences_rank(graph)
    sent_selected = nlargest(5, zip(scores, count()))
    sent_index = []
    for i in range(5):
            sent_index.append(sent_selected[i][1])
    print([sents[i] for i in sent_index])
    break


