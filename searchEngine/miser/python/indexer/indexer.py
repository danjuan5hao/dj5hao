# -*- coding: utf-8 -*-
from itertools import accumulate
import os

class PostingsList:  # 倒排列表

    def __init__(self, document_id, offsets_list, positions_count,
                 positions_list_next):
        self.document_id = document_id
        self.offsets_list = offsets_list
        self.positions_count = positions_count
        self.positions_list_next = positions_list_next

    def __iter__(self):
        yield self.positions_list_next

    def __repr__(self):
        return f"{self.offsets_list}"

class InvertedIndexHash:  # 倒排文件

    def __init__(self,
                 token_id=None,
                 token_text=None,
                 postings_list=None,
                 docs_count=None,
                 postings_count=None):
        self.token_id = token_id
        self.token_text = token_text
        self.postings_list = postings_list
        self.docs_count = docs_count
        self.postings_count = postings_count

    def __repr__(self):
        return self.token_text

class InvertedIndexHashList:
    def __init__(self):
        self.indices = []
    
    def __len__(self):
        return len(self.indices)

    def __iter__(self):
        for i in self.indices:
            yield i

    def add(self, invertedIndex):
        self.indices.append(invertedIndex)
        return
  
class Indexer:

    def __init__(self,
                 invertedIndex_buffer_list=None,
                 invertedIndex_buffer_doc_threshold=2,
                 db=None):
        if invertedIndex_buffer_list is None:
            self.invertedIndex_buffer_list = InvertedIndexHashList()
        else:
            self.invertedIndex_buffer_list = invertedIndex_buffer_list

        self.invertedIndex_buffer_doc_threshold = invertedIndex_buffer_doc_threshold
        self.invertedIndex_buffer_doc_count = 0
        self.db = db

    def add_document(self, document):
        """
        1. 取出词元
        2. 建立倒排列表，更新小倒排索引
        3. 小倒排索引增长到一定的大小， 和存储器上的倒排索引合并
        """
        self._text_to_postings_lists(document, self.invertedIndex_buffer_list)
        self.invertedIndex_buffer_doc_count += 1

        if self.invertedIndex_buffer_doc_count > self.invertedIndex_buffer_doc_threshold:
            self._update_db_postings(self.invertedIndex_buffer_list, self.db)
        return

    def _text_to_postings_lists(self, document, invertedIndex_buffer):
        """为文档内容建立倒排列表的集合, 
        先建立一个document级别的倒排文件（doc_invertedIndex），之后和缓冲倒排文件合并"""

        tokens = self._get_all_tokens_from_document(document)
        document_id = self._get_document_id(document)

        doc_invertedIndex = self._tokens_to_invertedIndex(tokens, document_id)
        print(len(doc_invertedIndex))
        for invertedIndex in doc_invertedIndex:
            print(invertedIndex.token_text)
            p = invertedIndex.postings_list
            p_next = p.positions_list_next
            while p_next is not None:
                print("HERE")
                print(p.document_id)
                print(p.offsets_list)

                p = p_next 
                p_next = positions_list_next

        exit()

        
    
        # 这里可以直接合并各个token的倒排列表，到一个doc_倒排文件，再合并doc文件到buffer文件上
        # 或者直接把token倒排list合并到buffer倒排文件上
        # 比较方案 1： 效率速度， 2遇到错误时候的反应

        # 只能去合并两个倒排索引，
        # 也可以合并两个倒排列表，只要把他们连起来就行了，但是这时候就必须要更新 它对应的倒排缩引的相关值。
        # 包括总的文档数，总的倒排项数量。
        self._merge_inverted_index(doc_invertedIndex, invertedIndex_buffer)
        return 

    def _get_all_tokens_from_document(self, document):
        all_token = document[0].split()
        all_position = [0]
        all_position.extend([*map(len, all_token)][:-1])
        all_token_position = accumulate(all_position)
        return list(zip(all_token, all_token_position))

    def _get_document_id(self, document):
        document_id = document[1]
        return document_id

    def _tokens_to_invertedIndex(self, tokens, document_id):
        """为文档中的所有词元船舰倒排列表,组成文档级别的倒排索引
        """,
        tmp_invertedIndex_list = InvertedIndexHashList()
        for token in tokens:
            self._renew_doc_invertedIndex_on_token(token, document_id,
                                         tmp_invertedIndex_list)
            
        return tmp_invertedIndex_list

    def _renew_doc_invertedIndex_on_token(self, token, document_id,
                                doc_invertedIndex_list):
        """
        更新倒排索引，
        """
        token_text, token_position = token
        token_invertedIndex = self._get_invertedIndex_by_token(token_text, doc_invertedIndex_list)

        positionList = PostingsList(document_id, [token_position], 1, None)
 
        self._add_postionList_to_invertedIndex(positionList,  token_invertedIndex)
        return 
    
    def _get_invertedIndex_by_token(self, token_text, doc_invertedIndex_list):
        for invertedIndex in doc_invertedIndex_list:
            if token_text == invertedIndex.token_text:
                return invertedIndex
        else:
            tmp_invertedIndex = InvertedIndexHash(token_text=token_text)
            doc_invertedIndex_list.add(tmp_invertedIndex)
            return tmp_invertedIndex

    def _add_postionList_to_invertedIndex(self, positionList, invertedIndex):
        p = invertedIndex.postings_list
        if p is None:
            invertedIndex.postings_list = positionList
            return 
        else:
            
            while p is not None:
                if p.document_id == positionList.document_id:
                    p.offsets_list.extend(positionList.offsets_list)
                    p.positions_count += positionList.positions_count
                    return
                else:
                    p_prev = p 
                    p = p.positions_list_next
            p_prev.positions_list_next =  positionList
            return 


    def _merge_inverted_index(self, invertedIndexListOne, invertedIndexListTwo):
        """
        1. 按照token对齐
        2. 倒排列表+（检查重复？？？， doc_id）
        3. 倒排索引中 文档数 更新， 共出现的位置数 更新
        """
        pass 

    def _update_db_postings(self, ):  # 把倒排列表存更新到db中
        """"""
        return


if __name__ == "__main__":
    root = r"D:\BaiduNetdiskWorkspace\数据集"
    data_path = os.path.join(root, "Fudan/train/C32-Agriculture/utf8")

    # test_tokenizer = 

    filenames = os.listdir(data_path)
    for filename in filenames[:10]:
        print(filename)