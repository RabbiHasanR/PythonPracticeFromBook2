sentence='the quick brown fox jumps over the lazy dog'
words=sentence.split()
words_length=[len(word) for word in words if word!='the']
print(words)
print(words_length)
