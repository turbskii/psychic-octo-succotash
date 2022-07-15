dictionary_words = dict()
count = 0
fhand = open('mbox.txt')

for text in fhand:
    lowtext = text.lower()  # makes text lowercase
    #print(lowtext)
    for text in text:
        lettertext = text.join([i for i in text if i.isalpha()])
        #print(lettertext) #removes all non letters
        for letter in lettertext:
            dictionary_words [letter] = dictionary_words.get(letter,0) + 1
print(dictionary_words)
