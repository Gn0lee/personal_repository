import sys
input = sys.stdin.readline
from heapq import heappop,heappush


a,b = map(int,input().split())

gems = []
bags = []

for _ in range(a):
    w , v = map(int,input().split())
    heappush(gems,[w,v])

for __ in range(b):
    heappush(bags,int(input()))


result = 0
tmp = []
for ___ in range(b):

    capacity = heappop(bags)
   
    while gems and gems[0][0] <= capacity:
        weight , value = heappop(gems)
        heappush(tmp,-value)

    if tmp:
        result += -heappop(tmp)
    elif not gems:
        break

print(result)