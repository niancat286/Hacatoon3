class WordIterator:
    def __init__(self, text):
        self.text = text
        self.chars = list(text)
        self.position = 0
        self.current_word = ""

    def __next__(self):
        punctuation = '.,!?;:-()[]{}"\' '
        while self.position < len(self.chars) and self.chars[self.position] in punctuation:
            self.position += 1
        if self.position >= len(self.chars):
            raise StopIteration

        self.current_word = ""
        while (self.position < len(self.chars) and self.chars[self.position] not in punctuation): self.current_word += self.chars[self.position]
        self.position += 1
        return self.current_word


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
