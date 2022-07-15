dictionary_words = dict()

fhand = open('mbox.txt')


for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    for time in words:
        time = words[5]
        #print(time)
        for hour in time:
            splitat = 2
            hour = time[:splitat]
            #print (hour)
            dictionary_words [hour] = dictionary_words.get(hour,0) + 1

print(dictionary_words)
