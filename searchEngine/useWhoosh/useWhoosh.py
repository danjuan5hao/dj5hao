# -*- coding: utf-8 -*-
from whoosh.index import create_in
from whoosh import index
from whoosh.qparser import QueryParser
import copy


class UseWhoosh:
    def __init__(self, doc_parser, ix_path):
        self.doc_parser = doc_parser
        self.ix_path = ix_path
        self.qp = QueryParser("content", schema=doc_parser.schema)
        self.load_or_create_ix(ix_path)

    def load_or_create_ix(self, ix_dir):
        schema = self.doc_parser.schema
        try:
            self.ix = index.open_dir(ix_dir)
            print("HERE")

        except:
            self.ix = create_in(ix_dir, schema)

    def add_documents(self, documents):
        writer = self.ix.writer()
        for document in documents:
            author, title, content = self.doc_parser(document)
            writer.add_document(title=title, author=author, content=content)
        writer.commit()
        return

    def search_query(self, query):
        with self.ix.searcher() as searcher:
            query = self.qp.parse(query)
            rst = searcher.search(query, limit=10)
            rst = list(rst)
            print(rst[0])
        return rst


if __name__ == "__main__":
    from pparser import FudanParser


    import os 

    test_fudanparser = FudanParser()
    root = r"D:\BaiduNetdiskWorkspace\数据集"
    path = os.path.join(root, r"Fudan\train\C32-Agriculture\utf8")
    file_names = os.listdir(path)

    test_useWhoosh = UseWhoosh(test_fudanparser, "searchEngine/useWhoosh/index")
    file_paths = [os.path.join(path, file) for file in file_names]
    test_useWhoosh.add_documents(file_paths)

    rst = test_useWhoosh.search_query("农业")


