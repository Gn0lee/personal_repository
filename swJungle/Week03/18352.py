import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,k):
    
    q = deque([])
    q.append(x)
    chk[x] = True
    distance[x] = 0

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not chk[i]: 
                q.append(i)
                chk[i] = True
                distance[i] = distance[now] + 1 ## now에서 i까지 거리는 1이므로 now까지의 거리에서 1을 추가해준다.
                if distance[i] == k:
                    result.append(i)           


result = []
n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
chk = [False]*(n+1)
distance = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

bfs(x,k)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    print(*result,sep="\n")