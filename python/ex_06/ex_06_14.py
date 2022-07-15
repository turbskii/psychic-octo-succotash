data = 'X-DSPAM-Confidence:0.8475 '
colon = data.find(':')
#print (colon)
acolon = data.find(' ',colon)
#print(acolon)
num = data[colon+1:acolon]
fnum =float(num)
print(fnum)
