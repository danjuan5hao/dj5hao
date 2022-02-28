# -*- coding: utf-8 -*-
class Searcher:
    def __init__(self):
        pass 

    def search(self, query):
        query_tokens = self._split_query_into_tokens(query)
        results = self._search_docs(query_tokens)
        pass 

    def _search_docs(self, query_tokens):
        pass
    
     