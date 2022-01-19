from utils import cosine_similarity
import jieba

def read(path):  # 读取txt文件，并返回list
        f = open(path, encoding="utf8")
        data = []
        for line in f.readlines():
            data.append(line)
        return data



    
def use_expand(model,title_):
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

def compute_similarity_by_avg(model,sents_1, sents_2):

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