from collections import deque
import sys
from bisect import bisect_right,bisect_left
tower_num = int(input())
towers = list(map(int,sys.stdin.readline().split()))
towers = deque(towers)
ans= [0]*tower_num

index = tower_num

while towers:
    current_tower = towers.pop()
    
    for i in range(index-2,-1,-1):
        if current_tower < towers[i]:
            ans[index-1] = i+1
            break

    index -= 1

print(*ans)