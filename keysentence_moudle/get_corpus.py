from utils import read
import jieba
class Corpus:
    def __init__(self,stop_path):
        self.stop_path = stop_path
    

    def getstopword(self): # 获取停用词表
        swlis = []
        for i in read(self.stop_path):
            outsw = str(i).replace('\n', '')
            swlis.append(outsw)
        return swlis
    
    def getridofsw(self,lis, swlist):  # 去除文章中的停用词
        afterswlis = []
        for i in lis:
            if str(i) in swlist:
                continue
            else:
                afterswlis.append(str(i))
        return afterswlis
    

    def toword(self,txtlis):  # 将一片文章切割成词表，返回list
        wordlist = []
        alltxt = ''
        for i in txtlis:
            alltxt = alltxt+str(i)
        ridenter = alltxt.replace('\n', '')
        wordlist = jieba.lcut(ridenter)
        # wordlist = ridenter.split('。')
        return wordlist
    
    def corpus(self,filelist, swlist):  # 建立语料库
        alllist = []
        for i in filelist:
            afterswlis = self.getridofsw(self.toword(i), swlist)
            alllist.append(afterswlis)
        return alllist
    
    # def pec_sent(self,filelist, swlist):


    def corpus_st(self,filelist, swlist):  # 建立语料库
        alllist = []
        pec_all = []
        for i in filelist:
            afterswlis = self.getridofsw(self.toword(i), swlist)
            pec_all.append((len(i)-len(afterswlis))/len(afterswlis))
            alllist.append(afterswlis)
        return alllist,pec_all
    

    def preprocess(self,filelist):

        # swpath = self.stop_path
        swlist = self.getstopword()  # 获取停用词表列表

        corpuslist = self.corpus(filelist, swlist)  # 建立语料库
        

        return corpuslist

    def preprocess_st(self,filelist):

        # swpath = self.stop_path
        swlist = self.getstopword()  # 获取停用词表列表

        corpuslist,pec = self.corpus_st(filelist, swlist)  # 建立语料库
        

        return corpuslist,pec
    
    # def build_corpus(self,corpuslist):

    #     for item in self.preprocess():


