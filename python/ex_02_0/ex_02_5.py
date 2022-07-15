tc = input('What is the temperature in Celsius?\n')

try:
    fc = float(tc)
except:
    print('please enter a numerical value')
    quit()
tf = (fc * 1.8) + 32
print('Fahrenheit', tf)
