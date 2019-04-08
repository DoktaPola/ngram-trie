import math

capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyz'


def split_by_sentence(text: str) -> list:
    finale_list = []
    mid_list = []
    word_constr = ''
    new_text1 = text.replace('\n', ' ')
    new_text = new_text1.replace('  ', ' ')
    for index, letter in enumerate(new_text):
        if letter in ['.', '?', '!'] and index == len(new_text) - 1:
            mid_list.append(word_constr)
            mid_list.append('</s>')
            finale_list.append(mid_list)
            break
        if not mid_list:
            mid_list.append('<s>')
        if letter != " ":
            if letter in ['.', '?', '!'] and new_text[index + 1] == ' ' and new_text[index + 2] in capital_letters:
                mid_list.append(word_constr)
                mid_list.append('</s>')
                finale_list.append(mid_list)
                word_constr = ''
                mid_list = []
            else:
                if letter in capital_letters:
                    word_constr += letter.lower()
                elif letter in letters:
                    word_constr += letter
        else:
            if not word_constr:
                continue
            else:
                mid_list.append(word_constr)
                word_constr = ''
    return finale_list


class WordStorage:
    def __init__(self):
        self.storage = {}
        self.id = 0

    def from_corpus(self, corpus: tuple):
        for word in corpus:
            self.put(word)

    def put(self, word: str) -> int:
        if word not in self.storage.keys():
            self.storage[word] = self.id
            self.id += 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word in self.storage:
            return self.storage[word]

    def get_original_by(self, id: int) -> str:
        name = ''
        for el in self.storage:
            if self.storage[el] == id:
                name = el
                break
            else:
                name = None
        return name


def encode(storage_instance, corpus) -> list:
    encode_arrays = []
    id_arr = []
    for sent in corpus:
        for word in sent:
            word_id = storage_instance.get_id_of(word)
            id_arr.append(word_id)
        encode_arrays.append(id_arr)
        id_arr = []
    return encode_arrays


class NGramTrie:
    def __init__(self, size):
        self.size = size  # 2,3,n-gram
        self.gram_frequencies = {}
        # self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        index = 0
        while index <= len(sentence) - self.size:
            pair = tuple([sentence[index], sentence[index + 1]])
            index += 1
            if pair in self.gram_frequencies.keys():
                self.gram_frequencies[pair] += 1
            else:
                self.gram_frequencies[pair] = 1
        return 'OK'
        # return 'ERROR'


if __name__ == '__main__':
    with open('hi.txt', 'r') as f:  # not_so_big_reference_text
        REFERENCE_TEXT = f.read()

# sentences = split_by_sentence(REFERENCE_TEXT)
# ws = WordStorage()
# for sentence in sentences:
#     ws.from_corpus(tuple(sentence))
# ngram = NGramTrie(2)
# encoded = encode(ws, sentences)
# print(encoded)
# for enc in encoded:
#     ngram.fill_from_sentence(tuple(enc))

ngram = NGramTrie(2)
sentence = (1, 2, 1, 2, 1, 2)
print(ngram.fill_from_sentence(sentence))

# sentences = split_by_sentence(REFERENCE_TEXT)  # don't take the big original text, I tested on the first 500 lines
# ws = WordStorage()
# for sentence in sentences:
#     ws.from_corpus(tuple(sentence))
# ngram = NGramTrie(3)
# encoded = encode(ws, sentences)
# print(encoded)
# for enc in encoded:
#     ngram.fill_from_sentence(tuple(enc))
# ngram.calculate_log_probabilities()
# word1 = ws.get_id_of('she')
# word2 = ws.get_id_of('will')
# # word3 = ws.get_id_of('not')
# words = ngram.predict_next_sentence((word1, word2,))
# for word in words:
#     print(ws.get_original_by(word))
