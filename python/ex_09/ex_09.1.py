count = 0
dictionary_words = dict()
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue
        dictionary_words[word] = count

if 'the' in dictionary_words:
    print('true')

else:
    print('false')
