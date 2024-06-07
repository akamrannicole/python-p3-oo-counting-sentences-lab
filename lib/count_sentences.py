# lib/count_sentences.py

class MyString:
    def __init__(self, value=""):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value
    
    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        # Split by sentence-ending punctuation marks followed by a space or end of string.
        sentences = [s for s in self._value.split() if s.endswith(('.', '!', '?'))]
        return len(sentences)
