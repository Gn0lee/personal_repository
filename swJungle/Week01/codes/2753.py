year = int(input())
dividing_4 = (year%4 == 0)
dividing_100 = (year%100 == 0)
dividing_400 = (year%400 == 0)
if(dividing_400):
    print("1")
elif(dividing_4 & (not dividing_100)):
    print("1")
else:
    print("0")