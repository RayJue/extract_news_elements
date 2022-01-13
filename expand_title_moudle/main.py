
from gensim.models import word2vec
from read_excel import get_news
import jieba

news = get_news()
titles,contents = news.titles_texts()
model = word2vec.Word2Vec.load('/home/rayjue/extract_news/news.model')

for item in titles:
    expand_title = []
    title = jieba.lcut(item)
    for i in title:
        try:
            expand_title.append(i)
            sim = model.most_similar(i, topn=2)
            for key in sim:
                expand_title.append(key[0])
        except:
            print(' 训练语料未发现该词语')
    print(title)
    print(expand_title)
    break





