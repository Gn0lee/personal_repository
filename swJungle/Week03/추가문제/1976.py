import sys
input = sys.stdin.readline

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
m = int(input())

parent = [0] *n

for k in range(n):
    parent[k] = k

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,input().split()))

check_list = list(map(int,input().split()))

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            union_parent(parent,y,x)

for a in range(len(check_list)-1):
    if find_parent(parent,check_list[a]-1) != find_parent(parent,check_list[a+1]-1):
        print("NO")
        exit(0)

print("YES")