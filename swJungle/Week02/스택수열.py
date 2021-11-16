import sys
from collections import deque


n = int(input())
n_list = deque([int(sys.stdin.readline()) for _ in range(n)])

stack = []
result = []

for i in range(1,n+1):
    if n_list[0] >= i:
        stack.append(i)
        result.append("+")
    while stack and n_list and stack[-1] == n_list[0] :
        
        stack.pop()
        result.append("-")
        n_list.popleft()

if stack:
    print("NO")
else:
    print(*result,sep="\n")

