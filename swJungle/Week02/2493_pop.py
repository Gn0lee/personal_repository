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
    
    # b = 1
    for i in range(index-2,-1,-1):
        if current_tower < towers[i]:
            ans[index-1] = i+1
            break

    
    
    # while copy_towers:
    #     a = copy_towers.pop()
    #     if current_tower < a:
    #         ans[index-1] = index - b
    #         b += 1
    #         break
    #     else:
    #         b += 1
    index -= 1

print(*ans)