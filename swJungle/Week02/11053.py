import sys
from bisect import bisect_left

N = int(input())
A_list = list(map(int,sys.stdin.readline().split()))

max_ans = 0
lis = []

for num in A_list:
    if not lis:
        lis.append(num)
        max_ans += 1
        continue
    if lis[-1] < num:
        lis.append(num)
        max_ans += 1
    else:
        lis[bisect_left(lis,num)] = num


print(max_ans)