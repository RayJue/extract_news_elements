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


    def preprocess(self,filelist):

        # swpath = self.stop_path
        swlist = self.getstopword()  # 获取停用词表列表

        corpuslist = self.corpus(filelist, swlist)  # 建立语料库
        

        return corpuslist
    
    def write_corpus(self,filelist):
        swlist = self.getstopword()  # 获取停用词表列表

        corpuslist = self.corpus(filelist, swlist)  # 建立语料库


        with open('/home/rayjue/extract_news/corpus.txt','w',encoding = 'utf-8') as fd:
            for item in corpuslist:
                fd.write(' '.join(item))
                fd.write('\n')
        
