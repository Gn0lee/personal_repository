import sys
from heapq import heapify, heappop, heappush
N = int(sys.stdin.readline())
card_list = []

for i in range(N):
    x = int(sys.stdin.readline())
    heappush(card_list,x)


ans = 0

while len(card_list) > 1 :
    a = heappop(card_list)
    b = heappop(card_list)
    ans += (a+b)
    heappush(card_list,a+b)


print(ans)