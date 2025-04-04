class SentenceIterator:
    def __init__(self, text):
        sentences = text.replace('!', '.').replace('?', '.').split('.')
        self.sentences = [s.strip() for s in sentences if s.strip()]
        self.index = 0

    def __next__(self):
        if self.index >= len(self.sentences):
            raise StopIteration
        sentence = self.sentences[self.index]
        self.index += 1
        return sentence

class Words:
    def __init__(self, text):
        self.sentence = text

    def __iter__(self):
        return SentenceIterator(self.sentence)
