from operator import lt


class LTP_ner_num:
    def __init__(self,ltp):
        self.ltp = ltp

    def get_num(self,sentence):

        seg, hidden = self.ltp.seg([sentence])
        ner = self.ltp.ner(hidden)

        return len(ner[0])


class LTP_Analysis:
    def __init__(self) -> None:
        pass

    def get_ner(self,sentence):

        seg, hidden = self.ltp.seg([sentence])
        ner = self.ltp.ner(hidden)

        return ner[0]
    
    def get_srl(self,sentence):

        seg, hidden = self.ltp.seg([sentence])
        srl = self.ltp.srl(hidden)

        return srl
    
    def get_dep(self,sentence):

        seg, hidden = self.ltp.seg([sentence])
        dep = self.ltp.dep(hidden)

        return dep