from random import random
from signal import pthread_kill
from ltp import LTP
from keywords_moudle.get_corpus import Corpus
from keywords_moudle.read_excel import get_news
from keyinfo_extract_moudle.analysis import LTP_Analysis
from keyinfo_extract_moudle.Extract_Elem import Extract_elements
news = get_news()
titles,contents = news.titles_texts()
stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
ltp = LTP()
nlp = LTP_Analysis()
Ex = Extract_elements(nlp,ltp)









