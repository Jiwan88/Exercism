import string

def split(word):
    return [char for char in word]

def is_pangram(sentence):
    sentence_letters = sorted(list(set(split(sentence.lower()))))
    if string.ascii_lowercase in ''.join(sentence_letters):
        return True
    return False

