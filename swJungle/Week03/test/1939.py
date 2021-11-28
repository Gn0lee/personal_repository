import sys
input = sys.stdin.readline
from collections import deque


inf = int(1e9)

def bfs(mid):
    q= deque([])

    visited = set()
    visited.add(s)
    q.append(s)

    while q:
        now = q.popleft()

        for w , i in graph[now]:
            if i not in visited and w >= mid:
                
                q.append(i)
                visited.add(i)

    if e in visited:
        return True
    else:
        return False
            
            



n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a ,b, c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

s,e = map(int,input().split())

start = 1
end = 1000000000
result = 1
while start <= end:
    mid = (start + end)//2

    if bfs(mid):
        start = mid + 1
        result = mid
    else:
        end = mid-1

print(result)

