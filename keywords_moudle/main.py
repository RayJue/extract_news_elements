from read_excel import get_news
from get_corpus import Corpus
from tfidf import tf_idf
import jieba

news = get_news()
titles,contents = news.titles_texts()

stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
tfidf = tf_idf()
# print(cor.preprocess(contents)[0])

for item in contents:
    corpus_words = cor.preprocess(contents)

    afterswlis = corpus_words[contents.index(item)]
    
    tfidfdic = tfidf.tf_idf(afterswlis, len(contents),corpus_words)  # 计算TF-IDF
    print(tfidfdic)
    break

