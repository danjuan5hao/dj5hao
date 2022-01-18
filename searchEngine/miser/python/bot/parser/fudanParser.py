# -*- coding: utf-8 -*-
from bot.parser.parser import Parser

class FudanParser(Parser):
    def __init__(self):
        super().__init__()

    def parse_one_text(self, text):
        return 