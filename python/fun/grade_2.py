def computergrade (core) :
    try:
        score = float(core)
        if score <= 1 and score >= 0.9:
            print('A')
        elif score < 0.9 and score >= 0.8:
            print('B')
        elif score < 0.8 and score >= 0.7:
            print ('C')
        elif score < 0.7 and score >= 0.6:
            print ('D')
        elif score < 0.6 :
            print ('F')
        elif score > 1:
            print ('Bad Score')
    except:
        print('Bad Score')
gd = input('What was the score?\n')
xp = computergrade(gd)
