ro = open('romeo.txt', 'r') # open file
text = ro.read()

#cleaning up

line = text.rstrip()
words = text.split()

unique = []
for word in words:
    if word not in unique:
        unique.append(word)

unique.sort()

print(unique)
