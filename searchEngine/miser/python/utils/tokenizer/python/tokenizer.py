# -*- coding; utf-8 -*- 
import jieba 

class Tokenzier:
    def __init__(self):
        pass

class JiebaTokenizer(Tokenzier):

    def __init__(self):
        self.jieba_tokenizer = jieba.lcut
    
    def tokenize(self, sentence):
        return self.jieba_tokenizer.__call__(sentence)

    


    