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

    if a <b:
        parent[b] = a
    else:
        parent[a] = b


computers = int(input())
lines = int(input())

parent = [0] * (computers+1)

for i in range(1,computers+1):
    parent[i] = i

for _ in range(lines):
    a , b = map(int, input().split())
    union_parent(parent,a,b)

for i in range(1,computers+1):
    find_parent(parent,i)

# print(parent)

print(Counter(parent)[1]-1)
print(len(Counter(parent)))