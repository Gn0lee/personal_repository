i = int(input())
hans = 99
if(1<=i<=99):
    print(i)
elif(100<=i<=110):
    print(99)
elif(i == 1000):
    print(144)
else:
    for x in range(110,i+1):
        
        x_100 = x // 100
        x_10 = (x%100-x%10)//10
        x_1 = x % 10

        if((x_100+x_1) == (x_10*2)):
            hans += 1
    print(hans)
