from collections.abc import Sequence
from collections import UserDict


class Sentence(Sequence):
    '''This inheritance adds additions functionality'''

    def __init__(self, source):
        self.text = source.strip().lower()
        self.words = self.text.split(' ')

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)


class MyDict(UserDict):
    '''Better to subclass UserDict than Dict'''

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


'''\
Dictionary methods keys(), values(), items() returns a view of the
dictionary without creating a copy of the data. They are instances of special
classes and can work with set operations.
'''



words = "Hello, this string was created for testing purpuses"
sentence = Sentence(words)

print(' '.join([word for word in sentence]))
print(sentence.count('string'))  # additional functionality
















