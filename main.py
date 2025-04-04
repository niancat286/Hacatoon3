import LongWordIterator_class
import SentenceIterator_class
import WordIterator_class
import WordStartsWithIterator_class


with open("import.txt", "r", encoding="utf-8") as f:
    text = f.read()


sentesce_iterator = SentenceIterator_class.Words(text)
long_word_iterator = LongWordIterator_class.Words(text)
word_iterator = WordIterator_class.Words(text)
word_starts_with_iterator = WordStartsWithIterator_class.Words(text, "п")


with open("output.txt", "w", encoding="utf-8") as f:

    f.write("\n===== Вивід WordIterator =====\n")
    for word in word_iterator:
        f.write(word + "\n")

    f.write("\n===== Вивід LongWordIterator =====\n")
    for word in long_word_iterator:
        f.write(word + "\n")

    f.write("\n===== Вивід WordStartsWithIterator =====\n")
    for word in word_starts_with_iterator:
        f.write(word + "\n")

    f.write("===== Вивід SentenceIterator =====\n")
    for sentence in sentesce_iterator:
        f.write(sentence + "\n")