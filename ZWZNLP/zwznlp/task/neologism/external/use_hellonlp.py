# -*- coding: utf-8 -*- 

from hellonlp.ChineseWordSegmentation import segment_entropy

if __name__ == "__main__":
    import pandas as pd
    import os, sys 
    data_root = r"D:\BaiduNetdiskWorkspace\数据集"
    data_path = "FinancialDatasets/data/SmoothNLP投资结构数据集样本1k.xlsx"
    data_path = os.path.join(data_root, data_path)
    corpus = pd.read_excel(data_path, engine="openpyxl")
    corpus = corpus["介绍"].dropna().tolist()
    words = segment_entropy.get_words(corpus)
    print(words)