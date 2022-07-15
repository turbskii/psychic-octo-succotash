gd = input('What was the score?\n')
try:
    dgd = float(gd)
    if dgd <= 1 and dgd >= 0.9:
        print('A')
    elif dgd < 0.9 and dgd >= 0.8:
        print('B')
    elif dgd < 0.8 and dgd >= 0.7:
        print ('C')
    elif dgd < 0.7 and dgd >= 0.6:
        print ('D')
    elif dgd < 0.6 :
        print ('F')
    elif dgd > 1:
        print ('Bad Score')
except:
    print('Bad Score')
