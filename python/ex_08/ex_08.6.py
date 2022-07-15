bo = open('mbox.txt')


#strip = box.strip()
#words = box.split()


count = 0

for line in bo:

    line = line.rstrip()
    wds = line.split()
    if len(wds) < 4 or wds[0] != 'From' :
        continue
    count = count + 1
    print(wds[1])
    print(count)
