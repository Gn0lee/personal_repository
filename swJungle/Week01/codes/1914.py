def hanoi(n,start,end,sub):
    if n == 1:
        print(start,end)
        return
    hanoi(n-1,start,sub,end)
    print(start,end)
    hanoi(n-1,sub,end,start)

i = int(input())
if(i<=20):
    print(2**i-1)
    hanoi(i,1,3,2)
else:
    print(2**i-1)
