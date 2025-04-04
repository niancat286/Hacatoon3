class WordStartsWithIterator:
    def __init__(self, text, letter):
        for ch in ".,!?":
            text_line = text.replace(ch, "")
        collection = text_line.strip().split()
        print(collection)
        self._index = 0
        self.collection = []
        for el in collection:
            self.collection.append(el)
        self.letter = letter.lower()

    def __next__(self):
        if self._index >= len(self.collection):
            raise StopIteration
        word = self.collection[self._index]
        self._index += 1
        if word.lower().startswith(self.letter):
            return word
        else:
            return next(self)


class Words:
    def __init__(self, text, letter):
        self.text = text
        self.letter = letter

    def __iter__(self):
        return WordStartsWithIterator(self.text, self.letter)

if __name__ == '__main__':
    text = "Це приклад тексту, який містить різні слова! Для прикладів "
    words = Words(text, "п")

    for word in words:
        print(word)
