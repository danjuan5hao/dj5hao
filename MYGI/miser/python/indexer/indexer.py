# -*- coding: utf-8 -*-
from itertools import accumulate
import os
import re


class PostingsNode:  # 倒排列表项
    def __init__(self,
                 document_id,
                 sentence_ids,
                 sentence_count,
                 offsets,
                 positions_count,
                 posting_node_next=None):
        self.document_id = document_id  # 文档的id
        self.sentence_ids = sentence_ids  # 出现token的句子id
        self.sentence_count = sentence_count  # 出现token的句子的数量
        self.offsets = offsets  # token在文档中出现的位置（全文， 句子）
        self.positions_count = positions_count  # token一共在文档中出现了几次
        self.posting_node_next = posting_node_next  # 下指向一篇文档的倒排项


class InvertedIndex:  # 倒排索引
    def __init__(self,
                 token_id=None,
                 token_text=None,
                 postings_node=None,
                 docs_count=None,
                 positions_count=None):  #
        self.token_id = token_id  # token的id
        self.token_text = token_text
        self.postings_node = postings_node  # 第一个倒排项
        self.docs_count = docs_count  # 出现token的文档数量
        self.positions_count = positions_count  # 一共出现token的次数

    def __repr__(self):
        return self.token_text


class InvertedIndexDict:
    def __init__(self):
        self.indices = {}

    def __len__(self):
        return len(self.indices)

    def __iter__(self):
        for i in self.indices:
            yield i

    def add_index(self, index):
        pass


class Indexer:
    """
    构建文档的倒排索引，然后合并到磁盘上【目前是数据库】
    """
    def __init__(
        self,
        invertedIndexDict_buffer,
        invertedIndexDict_buffer_threshold,
        # 这里按照文档的数量作为阈值，但是应该是存储空间不足了，然后进行缓存。
    ):
        self.invertedIndexDict_buffer = invertedIndexDict_buffer
        self.invertedIndexDict_buffer_threshold = invertedIndexDict_buffer_threshold
        self.invertedIndexDict_buffer_count = 0

    def add_document(self, document, document_db, index_db):
        """
        1. 取出词元
        2. 建立倒排列表项，更新该文档的倒排索引
        3. 文档倒排索引和内存倒排索引合并
        4. 内存倒排索引增长到一定的大小， 和存储器上的倒排索引合并
        """
        # document_id = self._save_doucment_db(document, document_db)
        document_id = 2
        doc_invertedIndexDict = self._document_to_doc_invertedIndexDict(
            document, document_id)
        self._merge_doc_buffer(doc_invertedIndexDict,
                               self.invertedIndexDict_buffer)

        self.invertedIndex_buffer_doc_count += 1

        if self.invertedIndex_buffer_doc_count > self.invertedIndex_buffer_doc_threshold:
            self._update_db_postings(self.invertedIndexDict_buffer, index_db)
        return

    def _save_document_db(self, document, document_db):
        pass

    def _document_to_doc_invertedIndexDict(document, document_id):
        doc_invertedIndexDict = InvertedIndexDict()
        tokens = self._tokenize_document(document)
        self._tokens_to_invertedIndexDict(tokens, doc_invertedIndexDict,
                                          document_id)
        return doc_invertedIndexDict

    # def _split_document(self, document):
    #     pass

    def _tokenize_document(self, document):
        chars = [char for char in document]
        return chars

    def _tokens_to_invertedIndexDict(self, tokens, document_id,
                                     invertdIndexDict):
        sentence_offset = 0
        document_offset = 0
        for token in tokens:
            token_sentence_offset = sentence_offset
            token_document_offset = document_offset

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
        token_invertedIndex = self._get_invertedIndex_by_token(
            token_text, doc_invertedIndex_list)

        positionList = PostingsList(document_id, [token_position], 1, None)

        self._add_postionList_to_invertedIndex(positionList,
                                               token_invertedIndex)
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
            p_prev.positions_list_next = positionList
            return

    def _merge_inverted_index(self, invertedIndexListOne,
                              invertedIndexListTwo):
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
    test_invertedIndexDict = InvertedIndexDict()
    test_indexer = Indexer(test_invertedIndexDict, 2)

    filenames = os.listdir(data_path)
    for filename in filenames[:10]:
        file_path = os.path.join(data_path, filename)
        with open(file_path, 'r', encoding="utf-8") as f:
            doc = "".join(f.readlines())
            test_indexer.add_document(file_path)
        # with open(file_path, 'r', encoding="utf-8") as f:
