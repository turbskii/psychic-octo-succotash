shout = input('Enter a file name\n')

try:
    fshout = open(shout,'r')

except:
    print ('File cannot be opened', shout)
    exit()

file_contents = fshout.read()


new_fshout = file_contents.upper()
print(new_fshout)
