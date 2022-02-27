# -*- coding: utf-8 -*-
class Document:
    def __init__(self, document_id, title, body):
        self.document_id = document_id
        self.title = title
        self.body = body
        self.title_size = len(title)
        self.body_size = len(body)
 
