"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    pass
    # with open('not_so_big_reference_text.txt', 'r') as f:
    #     REFERENCE_TEXT = f.readlines()
    #     TEXT = " ".join(REFERENCE_TEXT)


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        pass

    def get_id_of(self, word: str) -> int:
        pass

    def get_original_by(self, id_word: int) -> str:
        pass

    def from_corpus(self, corpus: tuple):
        pass


class NGramTrie():
    def __init__(self, n):
        pass

    def fill_from_sentence(self, sentence: tuple) -> str:
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass


def encode(storage_instance, corpus) -> list:
    pass


def split_by_sentence(text: str) -> list:
    pass
