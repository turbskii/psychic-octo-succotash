def chop(t):
    del t[0]
    del t[-1]

#def middle(t):
    #new = t[1:]
    #del new[-1]
    #return new


numlist = list()
while True:
    inp = input ('enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
    #print(numlist)


xp = chop(numlist)
print(xp)


#yp = middle(numlist)


#print(yp)
