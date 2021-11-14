from collections import deque

tower_num = int(input())
towers = list(map(int,input().split()))
towers = deque(towers)
ans= [0]*tower_num

cnt = tower_num - 1

while cnt > 0:
    current_tower = towers[-1]
    towers.appendleft(towers.pop())

    for i in range(1,cnt+1):
        if i == cnt:
            towers.appendleft(towers.pop())
            if towers[-1] > current_tower:
                ans[cnt] = cnt-i
                towers.rotate(-i)
                break
            else:
                towers.rotate(-i)
        elif i == 1:
            if towers[-1] > current_tower:
                ans[cnt] = cnt
                break
            towers.appendleft(towers.pop())
            if towers[-1] > current_tower:
                ans[cnt] = cnt-i
                towers.rotate(-i)
                break
    
    
    cnt -= 1
print(*ans)