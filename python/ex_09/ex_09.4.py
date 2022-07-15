dictionary_words = dict()

fhand = open('mbox.txt')


for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_words:
            dictionary_words[words[1]] = 1
        else:
            dictionary_words[words[1]] += 1

bigcount = None
bigwords = None
for words, count in dictionary_words.items():
    if bigcount is None or count > bigcount:
        bigword = words
        bigcount = count
print (bigword, bigcount)
