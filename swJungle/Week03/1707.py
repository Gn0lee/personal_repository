import sys
input = sys.stdin.readline

def find_parent(x,parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x],parent)
    
    return parent[x]

def union_parent(a,b,parent):
    a = find_parent(a,parent)
    b = find_parent(b,parent)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b



k = int(input())
for _ in range(k):
    v ,e = map(int,input().split())
    parent = [0] *(v+1)
    for i in range(1,v+1):
        parent[i] = i
    chk = True
    for _ in range(e):
        a , b = map(int,input().split())
        if find_parent(a,parent) != find_parent(b,parent):
            union_parent(a,b,parent)
        else:
            chk = False
            break
    if chk:
        print("YES")
    else:
        print("NO")