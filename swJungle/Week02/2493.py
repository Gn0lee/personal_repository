from collections import deque

tower_num = int(input())
towers = list(map(int,input().split()))

ans= [0]*tower_num
stack = []


for i,h in reversed(list(enumerate(towers))):
    
    search = i -1
    while search >= 0:
        if towers[search] > h:
            break
        else:
            search -= 1

    ans[i] = search + 1



print(*ans)