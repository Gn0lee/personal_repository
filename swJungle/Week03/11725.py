import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i] = i

nodes = []

for _ in range(n-1):

    a , b = map(int,input().split())
    # if a > b:
    #     nodes.append((b,a))
    # else:
    #     nodes.append((a,b))
    nodes.append((a,b))
# nodes = sorted(nodes)
nodes = sorted(nodes)
q = deque(nodes)

for node in nodes:
    a, b = node
    if a == 1:
        parent[b] = 1
    elif b == 1:
        parent[a] = 1
    elif parent[a] != a and parent[b] == b:
        parent[b] = a
    elif parent[b] != b and parent[a] == a:
        parent[a] = b


# while q:
#     a,b = q.popleft()
#     if a == 1:
#         parent[b] = 1
#         continue
#     elif b == 1:
#         parent[a] = 1
#         continue
#     elif parent[a] != a and parent[b] == b:
#         parent[b] = a
#         continue
#     elif parent[b] != b and parent[a] == a:
#         parent[a] = b
#         continue
#     else:
#         q.append((a,b))


print(*parent[2:],sep="\n")