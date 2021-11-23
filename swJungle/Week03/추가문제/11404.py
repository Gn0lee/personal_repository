import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = int(1e9)

graph = [[inf]*n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a , b ,c = map(int,input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

for k in range(n):
    for j in range(n):
        for i in range(n):
            graph[j][i] = min(graph[j][i],graph[j][k]+graph[k][i])

for y in range(n):
    for x in range(n):
        if graph[y][x] == inf:
            print(0, end=' ')
        else:
            print(graph[y][x],end=" ")
    print()