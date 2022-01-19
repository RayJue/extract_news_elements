from textrank4zh import TextRank4Keyword, TextRank4Sentence


class TextRank(object): 
    
    def __init__(self,text):
        super().__init__()
        self.text = text
        self.t4s = TextRank4Sentence(delimiters='。')
        self.t4s.analyze(text=text, lower=True, source="all_filters")
    
    def use(self):
        for item in self.t4s.get_key_sentences(num=len(self.text.split('。'))):
                yield (item.index, item.weight, item.sentence)


