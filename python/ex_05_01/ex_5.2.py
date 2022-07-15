largest = None
smallest = None
count = 0

while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break

    try:
            if count == 0:
                max = float(sval)
                min = float(sval)
                count = 1
            elif float(sval) > max:
                    max = float(sval)
            elif float(sval)< min :
                    min = float(sval)

    except:
        print('invalid input')
        continue

print ('Maximun: ' + str(max))
print ('Minimun: ' + str(min))
