import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c


for k in range(1,n+1):
    for j in range(1,n+1):
        for i in range(1,n+1):
            graph[j][i] = min(graph[j][i], graph[j][k]+graph[k][i])

### 3중 반복문이므로 노드의 수가 적을 때 효율적이다.