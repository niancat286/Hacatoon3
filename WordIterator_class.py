class WordIterator:
    def __init__(self, text_line):
        for ch in ".,!?;:-—()[]{}\"'«»…@#№$%^&*+=/\\|<>~`":
            text_line = text_line.replace(ch, "")
        collection = text_line.strip().split()
        #print(collection)
        self._index = 0
        self.collection = []
        for el in collection:
            self.collection.append(el)

    def __next__(self):
        if self._index >= len(self.collection):
            raise StopIteration

        current_word = self.collection[self._index]
        self._index += 1
        return current_word

class Words:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return WordIterator(self.text)

