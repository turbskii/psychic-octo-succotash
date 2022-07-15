look = input ('What is the name of the file?\n')
try:
    tlook = open(look, 'r')
except:
    print('cannot open file', look)
    exit ()

count = 0
total = 0

for line in tlook:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        strip = line.strip ()
        nline = strip.find (':')
        wstring = strip[nline + 2:]
        fstring = float(wstring)
        total = total + fstring

print(total/count)
