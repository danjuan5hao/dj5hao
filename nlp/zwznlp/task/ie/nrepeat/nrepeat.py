# -*- coding: utf-8 -*-

 


class Nrepeat:
    def __init__(self, search_engine, parser):
        self.search_engine = search_engine
        self.parser = parser         

    def find_query_entity_type(self, query):
        pass

    def add_document_by_path(self, document_path, document_parser):
        with open(document_path, 'r', encoding="utf-8") as f:
            document_parsed = document_parser(f)
    def add_document_parsed(self, ):
        pass 








if __name__ == "__main__":
    pass  

