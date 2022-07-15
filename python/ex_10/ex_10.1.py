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

lst = list()
for key, val in list(dictionary_words.items()):
    lst. append((val, key))

lst.sort(reverse = True)

print(lst)
