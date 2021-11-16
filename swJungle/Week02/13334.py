import sys
import heapq

n = int(sys.stdin.readline())
roads = []
ans = 0
roads_info = []
for i in range(n):
    house , office = list(map(int,sys.stdin.readline().split()))
    a = (house,office)
    roads.append(a)

d = int(sys.stdin.readline())

for road in roads:
    house , office = road
    if abs(house-office) <= d:
        road = sorted(road)
        roads_info.append(road)

roads_info.sort(key=lambda x : x[1])

heap = []
for road in roads_info:
    if not heap:
        heap.append(road)
    else:
        while heap and road[1] - heap[0][0] > d:
            heapq.heappop(heap)
            if not heap:
                break
        
        heapq.heappush(heap,road)
    ans = max(ans, len(heap))


print(ans)