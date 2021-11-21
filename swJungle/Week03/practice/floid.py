import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0   ## 자기자신은 0으로 설정(이런 경로는 없기때문)


for _ in range(m):
    a,b,c = map(int,input().split()) #a -> b 로 가는 비용 c를 그래프에 입력
    graph[a][b] = c


for k in range(1,n+1):
    for j in range(1,n+1):
        for i in range(1,n+1):
            graph[j][i] = min(graph[j][i], graph[j][k]+graph[k][i])  #j -> i vs j -> k -> i 의 거리를 비교하여 작은값을 입력

### 3중 반복문이므로 노드의 수가 적을 때 효율적이다.
### 노드의 개수가 500이하일때 사용가능