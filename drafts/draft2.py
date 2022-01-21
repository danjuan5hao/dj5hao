# -*- coding: utf-8 -*-
import re 

sentence = "我。 百事可乐。非常\n开心"
rst = re.split("(。|\n)", sentence)
# for i in range(len(rst, step=2)):
#     print(i)
print(rst)