# -*- coding: utf-8 -*-

from smoothnlp.algorithm.phrase import extract_phrase


if __name__ == "__main__":
    import pandas as pd
    data_path = r"D:\BaiduNetdiskWorkspace\数据集\FinancialDatasets\data\SmoothNLP投资结构数据集样本1k.xlsx"
    corpus = pd.read_excel(data_path, engine="openpyxl")
    corpus = corpus["介绍"].dropna().tolist()
    words = extract_phrase(corpus)
    print(words)