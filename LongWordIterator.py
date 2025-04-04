class WordStartsWithIterator:
    def __init__(self, text, letter):
        self.letter = letter.lower()
        self.word_iterator = WordIterator(text)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            word = next(self.word_iterator)
            if word.lower().startswith(self.letter):
                return word


class SentenceIterator:
    def __init__(self, sentence):
        sentences = text.replace('!', '.').replace('?', '.').split('.')
        self.sentences = [s.strip() for s in sentences if s.strip()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.sentences):
            sentence = self.sentences[self.index]
            self.index += 1
            return sentence
        else:
            raise StopIteration
