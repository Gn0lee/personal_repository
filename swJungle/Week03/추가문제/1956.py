import sys
input = sys.stdin.readline

inf = int(1e9)

v,e = map(int,input().split())

graph = [[inf]* v for _ in range(v)]

for _ in range(e):
    a , b , c = map(int,input().split())
    graph[a-1][b-1] = c

for k in range(v):
    for j in range(v):
        for i in range(v):
            graph[j][i] = min(graph[j][i],graph[j][k]+graph[k][i])

result = inf

for l in range(v):
    result = min(result,graph[l][l])

if result == inf:
    print(-1)
else:
    print(result)