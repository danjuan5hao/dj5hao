# -*- coding: utf-8 -*-
from whoosh.fields import Schema, ID, TEXT
from jieba.analyse import ChineseAnalyzer


class FudanParser:
    def __init__(self):
        self.schema = Schema(title=TEXT(stored=True, analyzer=ChineseAnalyzer()),
                             author=TEXT(stored=True),
                             content=TEXT(stored=True, analyzer=ChineseAnalyzer())
                            )


    def parse_from_path(self, path):
        author=""
        title=""
        text=[]

        with open(path, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                line=line.strip()
                if line.startswith("【 作  者 】"):
                    author=line.replace("【 作  者 】", "").strip()
                elif line.startswith("【 标  题 】"):
                    title=line.replace("【 标  题 】", "").strip()
                elif line.startswith("【 正  文 】"):
                    continue
                elif line.startswith("【"):
                    continue
                else:
                    text.append(line)
        text="".join(text)
        return author, title, text

    def __call__(self, path):
        return self.parse_from_path(path)

if __name__ == "__main__":
    test_path=r"D:\BaiduNetdiskWorkspace\数据集\Fudan\train\C16-Electronics\utf8\C16-Electronics18.txt"
    parser=FudanParser()
    rst=parser.parse_from_path(test_path)
    print(rst)
