from ltp import LTP
from get_corpus import Corpus
from read_excel import get_news


news = get_news()
titles,contents = news.titles_texts()
stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
ltp = LTP()   
for item in contents:

  
    seg, hidden = ltp.seg([item])
    pos = ltp.pos(hidden)
    ner = ltp.ner(hidden)
    srl = ltp.srl(hidden)
    dep = ltp.dep(hidden)
    sdp = ltp.sdp(hidden)
