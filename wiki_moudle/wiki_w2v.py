import os
import logging
import multiprocessing

from gensim.models import word2vec
from gensim.corpora import WikiCorpus

from utils import cht_to_chs_zhconv, cut_sentence, remove_non_chinese

LOG = logging.getLogger(__name__)


class ZhWiki_porcess(object):


    def __init__(self, corpus_path):


        # 生成结果文件路径
        self.corpus_path =corpus_path
        self.text_path = '/home/rayjue/extract_news/zhwiki.txt'
        self.model_path = '/home/rayjue/extract_news/wiki.model'


    def prepare_corpus(self):
        i = 0
        corpus_file = WikiCorpus(self.corpus_path,
                                 lemmatize=False, dictionary={})

        with open(self.text_path, 'wb') as text_file:
            for tokens in corpus_file.get_texts():
                line = ' '.join(tokens)
                line = cht_to_chs_zhconv(line)
                tokens = cut_sentence(line)
                tokens = remove_non_chinese(tokens)
                line = ' '.join(tokens) + '\n'
                text_file.write(bytes(line, encoding='utf-8'))
                i = i + 1
    


    def train_model(self):

        ls = word2vec.LineSentence(self.text_path)
        mdl = word2vec.Word2Vec(ls, size=300, window=5, min_count=10,
                                workers=multiprocessing.cpu_count())
        mdl.wv.init_sims(replace=True)
        mdl.save(self.model_path)
        mdl.wv.save_word2vec_format(self.vector_path, binary=False)