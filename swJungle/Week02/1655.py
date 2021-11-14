import heapq
import sys
from collections import deque
from heapq import heappop, heappush, _heapify_max, heappushpop

N = int(input())

min_heap = [] ## 최대의 최소값
max_heap = [] ## 최소의 최대값

for i in range(N):
    x = int(sys.stdin.readline())
    if i % 2 == 0:
        heapq.heappush(max_heap,-x)
    else:
        heapq.heappush(min_heap,x)
    if min_heap and max_heap and min_heap[0] < -max_heap[0]:
        y =heappushpop(min_heap,-heappop(max_heap))
        heappush(max_heap,-y)
    print(-max_heap[0])


