import sys
from collections import Counter
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



n,m = map(int,input().split())

parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a , b = map(int,input().split())
    union_parent(parent,a,b)
    
for i in range(1,n+1):
    find_parent(parent,i)


# print(parent)
# print(set(parent))
# print(len(set(parent))-1)
print(len(Counter(parent))-1)