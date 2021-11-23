import sys
input = sys.stdin.readline
from math import sqrt

def cal_dist(a,b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return sqrt(x**2 + y**2)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
star = []
graph = []
parent = [i for i in range(n)]
for _ in range(n):
    x , y = map(float,input().split())
    star.append([x,y])


for i in range(n-1):
    for j in range(i+1,n):
        graph.append([cal_dist(star[i],star[j]),i,j])

graph.sort()

ans = 0

for dist, a , b in graph:
    if find_parent(parent,a) != find_parent(parent,b):
        ans += dist
        union_parent(parent,a,b)

# print(graph)
# print(parent)
print(format(ans,".2f"))