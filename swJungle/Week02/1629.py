import math
A,B,C = list(map(int,input().split()))

def divid_multi(x,b,c) :
    global left
    
    if b == 1:   
        return x % c
    
    before = divid_multi(x,b//2,c)
    if b % 2 == 0:
        return before * before %c
    else:
        return before * before * x % c 

# multi(A,B,C)
ans = divid_multi(A,B,C)
# print(left%C)
print(ans)