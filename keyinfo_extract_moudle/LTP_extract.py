from random import random
from signal import pthread_kill
from ltp import LTP
from get_corpus import Corpus
from read_excel import get_news
import random

news = get_news()
titles,contents = news.titles_texts()
stop_path = '/home/rayjue/extract_news/stop_words.txt'
cor = Corpus(stop_path)
ltp = LTP()

class LTP_ner_num:
    def __init__(self) -> None:
        pass

    def get_num(self,sentence):

        seg, hidden = ltp.seg([sentence])
        ner = ltp.ner(hidden)

        return len(ner[0])


class LTP_Analysis:
    def __init__(self) -> None:
        pass

    def get_ner(self,sentence):

        seg, hidden = ltp.seg([sentence])
        ner = ltp.ner(hidden)

        return ner[0]
    
    def get_srl(self,sentence):

        seg, hidden = ltp.seg([sentence])
        srl = ltp.srl(hidden)

        return srl
    
    def get_dep(self,sentence):

        seg, hidden = ltp.seg([sentence])
        dep = ltp.dep(hidden)

        return dep


nlp = LTP_Analysis()

class Extract_elements:
    def __init__(self) -> None:
        pass
    
    def cal_elements(self,line):
        # for item in contents:

                    A0 =  []
                    A1 = []
                    LOC= []
                    TMP = []


                    sub_key = []
                    obj_key = []

            # for lines in item.split('。'):
                
                # for line in lines.split(','):
                    seg, hidden = ltp.seg([line])
                    dep = seg[0]
                    for itx in nlp.get_srl(line)[0]:
                        if len(itx):
                            for ix in itx:
                                if ix[0] in ['A0','A1','ARGM-LOC','ARGM-TMP']:
                                    if ix[0] == 'A0':
                                        A0.append(''.join(dep[ix[1]:ix[2]+1]))
                                    elif ix[0] == 'A1':
                                        A1.append(''.join(dep[ix[1]:ix[2]+1]))
                                    elif ix[0] == 'ARGM-LOC':
                                        LOC.append(''.join(dep[ix[1]:ix[2]+1]))
                                    elif ix[0] == 'ARGM-TMP':
                                        TMP.append(''.join(dep[ix[1]:ix[2]+1]))

                    for itd in nlp.get_dep(line)[0]:
                        if itd[-1] in ['SBV','VOB']:
                            if itd[-1] == 'SBV':
                                sub_key.append(''.join(dep[itd[0]:itd[1]+1]))
                            elif itd[-1] == 'VOB':
                                obj_key.append(''.join(dep[itd[1]-1:itd[0]]))
                    
                    if len(A0):
                        # print(max(A0,key=A0.count))
                        Sec_A0 = max(A0,key=A0.count)
                        
                    elif len(A1):
                        Sec_A0 = max(A1,key=A1.count)
                    elif len(sub_key):
                        Sec_A0 = max(sub_key,key=sub_key.count)
                    elif len(obj_key):
                        Sec_A0 = max(obj_key,key=obj_key.count)
                    else:
                        Sec_A0 = '没有该要素'
                    
                    if len(LOC):
                        Sec_LOC = max(LOC,key=LOC.count)
                    else:
                        Sec_LOC = '没有该要素'
                    
                    if len(TMP):
                        Sec_TMP = max(TMP,key=TMP.count)
                    else:
                        Sec_TMP = '没有该要素'

                    if len(obj_key):

                        Sec_Event = max(obj_key,key=obj_key.count)
                    elif len(sub_key):
                        Sec_Event = max(sub_key,key=sub_key.count)
                    
                    # print('Who:'+Sec_A0+'\t'+"where:"+Sec_LOC+'\t'+'when:'+Sec_TMP+'\t'+'event:'+Sec_Event)
                    return 'Who:'+Sec_A0+'\t'+"where:"+Sec_LOC+'\t'+'when:'+Sec_TMP+'\t'+'event:'+Sec_Event



