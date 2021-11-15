import sys
from heapq import heappop

N = int(input())
A_list = list(map(int,sys.stdin.readline().split()))

max_ans = 0
if N==1:
    max_ans = 1
else:
    while len(A_list) >1 :
        a = A_list.pop(0)
        b = [i for i in A_list]
        cnt = 1
        while b:
            x = heappop(b)
            if x > a :
                cnt += 1
                a = x
            else:
                cnt = 2
                a = x

        if cnt >= max_ans:
            max_ans = cnt        


print(max_ans)