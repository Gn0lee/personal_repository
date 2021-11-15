import sys
from collections import deque

while True:
    case = list(map(int,sys.stdin.readline().split()))
    if len(case) == 1:
        exit(0)
    n = case.pop(0)
    max_area = 0
    stack = []

    for i,h in enumerate(case):
        start = i   

        while stack and stack[-1][1] > h:
            index , height = stack.pop()
            max_area = max(max_area,height*(i-index))
            start = index
        stack.append((start,h)) 
    
    for i , h in stack:
        max_area = max(max_area,(n-i)*h)

    print(max_area)
