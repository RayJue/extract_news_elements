import  pandas  as pd
from utils import read

class get_news:
    def __init__(self):
        
        path = '/home/rayjue/extract_news/sina.xlsx'
        # self.news_path = news_path
        # self.stop_path = stop_path
        self.data = pd.read_excel(path)

    




    def titles_texts(self):
        titles = []
        contents = []

        for i in range(len(self.data.index.values)):
            titles.append(self.data.loc[i].values[-3].strip())
            contents.append(self.data.loc[i].values[-1].strip())
        
        return titles,contents
        