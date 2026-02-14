class SortSentence:
    def __init__(self, sentence):
        self.sentence = sentence
    def sort_words(self):
        words = self.sentence.split()
        words.sort()
        return words
sentence = input("Enter a sentence: ")
sorted_sentence = SortSentence(sentence)
print("Sorted words:", sorted_sentence.sort_words())