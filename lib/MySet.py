class MySet:

    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True  # Add a value as a key
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)  # Remove key if it exists
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()
        return self

    def __str__(self):
        return f"MySet: {{{', '.join(str(k) for k in self.dictionary)}}}"


    pass
