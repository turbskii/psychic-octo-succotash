dictionary_words = dict()

look = input('Please enter a file name\n')
try:
    olook = open(look, 'r')
except:
    print('file cannot be opened')
    exit()


for line in olook:
    #line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    else:
        if wds[2] not in dictionary_words:
            dictionary_words[wds[2]] = 1
        else:
            dictionary_words[wds[2]] += 1

print(dictionary_words)
