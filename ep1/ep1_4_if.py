#if else
leg = input()
leg = int(leg)
leg = float(leg)
if leg < 60:
    print('normal')
elif leg < 80:
    print('pretty')
else:
    print('beautiful')