import sys
input = sys.stdin.readline
from collections import deque

global minimum_cost
minimum_cost = 1e9

def bfs_bus(v):
    global minimum_cost

    q = deque([])
    chk[v] = True
    q.append([0,v])

    while q:
        now_cost,now = q.popleft()
        if now_cost > minimum_cost:
            return
        for i in bus_infos[now]:
            if not chk[i[1]] and i[1] != end:
                chk[i[1]] = True
                sum_cost = now_cost + i[0]
                if sum_cost > minimum_cost:
                    return
                i[0] = sum_cost
                q.append(i)
            elif not chk[i[1]] and i[1] == end:
                minimum_cost = min(now_cost + i[0],minimum_cost) 

n = int(input())
m = int(input())

bus_infos = [[] for _ in range(n+1)]
chk = [False] * (n+1)

for _ in range(m):
    a,b,cost = map(int,input().split())
    bus_infos[a].append([cost,b])

start, end = map(int,input().split())

bfs_bus(start)
print(minimum_cost)



