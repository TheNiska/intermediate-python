from collections.abc import Sequence


class Sentence(Sequence):
    '''This inheritance adds additions functionality'''

    def __init__(self, source):
        self.text = source.strip().lower()
        self.words = self.text.split(' ')

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)


words = "Hello, this string was created for testing purpuses"
sentence = Sentence(words)

print(' '.join([word for word in sentence]))
print(sentence.count('string'))  # additional functionality