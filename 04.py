Age=int(input('enter your age:-'))
if Age<15 and Age>60:
    print('not allowed')
elif Age>=15 and Age<25:
    print('ticket is 10 rupess')
elif Age>=25 and Age<45:
    print('ticket is 20 rupess')
elif Age>=45 and Age<60:
    print('ticket is 30 rupess')
else:
    print('ticket rupess is not mention')