import sys
import heapq

testcase = int(input())
heap = []
for _ in range(testcase):
    a = int(sys.stdin.readline())
    if a == 0 and len(heap) > 0:
        b = heapq.heappop(heap)
        print(b[1])
    elif a==0 and len(heap) == 0:
        print(0)
    else:    
        heapq.heappush(heap,(-a,a))
