sentence='the quick brown fox jumps over the lazy dog'
words=sentence.split()
words_length=[]
for word in words:
    if word!='the':
        words_length.append(len(word))

print(words)
print(words_length)
