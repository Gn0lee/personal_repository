import math

def Z(n,r,c):
    if(n==0):
        if(r==0 and c==0):
            
            return 0
        elif(r==0 and c==1):
            return 1
        elif(r==1 and c==0):
            return 2
        else:
            return 3
    else:
        if(r>=2**n and c >=2**n):
            return Z(n-1,r-2**n,c-2**n) + (4**n)*3
        elif(r>=2**n and c <2**n):
            return Z(n-1,r-2**n,c) + (4**n)*2
        elif(r<2**n and c >=2**n):
            return Z(n-1,r,c-2**n) + (4**n)*1
        else:
            return Z(n-1,r,c)

get_str = input().split()
# n = int(get_str[0])
r = int(get_str[1])
c = int(get_str[2])

if(r==0 or c==0):
    if(r == 0 and c !=0):
        n = int(math.log2(c))
    elif(c == 0 and r !=0):
        n = int(math.log2(r))
    else:
        n = 0
else:
    if(r>c):
        n = int(math.log2(r))
    elif(c<r):
        n = int(math.log2(c))
    else:
        n = int(math.log2(c))

print(Z(n,r,c))
print(n)
