ft = input('What is your temperature in Fahrenheit?\n')
try:
    tft = float(ft)
    if tft > 98.6:
        print ('You have a temperature and are going to die')
    elif tft <= 98.6 and tft > 95:
        print ('You do not have a temperature and will not die')
    elif tft <= 95:
        print ('You are hypothermic and will die')
except:
    print ('please use numerical values')
