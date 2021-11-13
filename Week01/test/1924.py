import calendar

month,day = map(int,input().split())


if calendar.weekday(2007,month,day) == 0:
    print('MON')
elif calendar.weekday(2007,month,day) == 1:
    print('TUE')
elif calendar.weekday(2007,month,day) == 2:
    print('WED')
elif calendar.weekday(2007,month,day) == 3:
    print('THU')
elif calendar.weekday(2007,month,day) == 4:
    print('FRI')
elif calendar.weekday(2007,month,day) == 5:
    print('SAT')
else:
    print('SUN')
