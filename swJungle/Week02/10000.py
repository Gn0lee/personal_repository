import sys
import collections
N = int(input())

v = 0
e = 0
f = 0
x_list = []

for i in range(N):
    x , r = list(map(int,sys.stdin.readline().split()))
    lower_x = x - r
    upper_x = x + r
    x_list.append(lower_x)
    x_list.append(upper_x)
    
x_list = collections.Counter(x_list)

for i in x_list.values():
    if i >=2:
        e += i
        v += 1



f = 2 -v +e
print(f)
