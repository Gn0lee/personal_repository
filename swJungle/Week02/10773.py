import sys
from collections import deque

k = int(input())
q = deque([])
k_list = [int(sys.stdin.readline()) for _ in range(k)]

for k in k_list:
    if k != 0:
        q.append(k)
    else:
        q.pop()

print(sum(q))