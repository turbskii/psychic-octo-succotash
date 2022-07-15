import re


hand = open('mbox.txt')
lst = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        for fx in x:
            fx = float(fx)
        lst.append(fx)
avg = sum(lst)/len(lst)
print(avg)
