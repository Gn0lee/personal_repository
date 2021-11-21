##미래도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
##방문 판매원 A는 현재 1번회사에 위치해 있으며, X 번 회사에 방문해 물건을 판매하고자한다.
##미래도시 도로는 양방향이며 연결되어 있다면 정확히 1만큼의 시간으로 이동할 수 있다.
##A는 1번회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는것이 목표이다. (최대한 빠르게 이동하고자 한다.)
##방문판매원이 회사사이를 이동하게 되는 최소시간을 계산하는 프로그램을 작성하시오
## N(회사수),M(경로수) 모두 100이하의 정수
## 둘째 줄부터 연결된 회사의 번호가 입력되며 마지막 줄에 X,K가 입력된다.

import sys
input = sys.stdin.readline
inf = int(1e9)
n , m = map(int,input().split())

graph = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a , b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x , K = map(int,input().split())

for i in range(n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for j in range(1,n+1):
        for i in range(1,n+1):
            
            graph[j][i] = min(graph[j][i],graph[j][k]+graph[k][i])

##플로이드 워셜 알고리즘을 수행하면 각 요소의 성분은 j에서 i로 가는 최단경로를 나타낸다

ans = graph[1][K] + graph[K][x]

if ans >= inf:
    print(-1)
else:
    print(ans)