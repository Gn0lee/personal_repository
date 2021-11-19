import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a <b:
        parent[b] = a
    else:
        parent[a] = b



v , e = map(int,input().split())

parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

infos = []

for i in range(e):
    a , b ,cost = map(int,input().split())
    infos.append((cost,a,b))

infos.sort()
result = 0
for cost, a, b in infos:
    if find_parent(parent,a) != find_parent(parent,b):
        result += cost
        union_parent(parent,a,b)

print(result)