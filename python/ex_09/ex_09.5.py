fhand = open('mbox.txt', 'r')

dictionary_words = dict()



for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    #print(words)
    for email in words:
        email = words[1]
        for domain in email:
            domain = email.split('@')[1]
            dictionary_words [domain] = dictionary_words.get(domain,0) + 1

print(dictionary_words)
