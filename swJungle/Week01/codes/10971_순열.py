import sys
from collections import deque
num_city = int(sys.stdin.readline())

cost_list = [list(map(int,sys.stdin.readline().split())) for i in range(num_city)]
chk = [False] * num_city

pos = [0]*(num_city)

global ans
ans = 10000000000

def set(i,n):
    global ans
    for j in range(n):
        if not chk[j] > 0:
            pos[i] = j
            if i == n-1:
                q = deque()
                for i in range(num_city-1):
                    if cost_list[pos[i]][pos[i+1]] != 0 and i < num_city -2:
                        q.append(cost_list[pos[i]][pos[i+1]])
                    elif cost_list[pos[i]][pos[i+1]] != 0 and i == num_city -2 and cost_list[pos[-1]][pos[0]] != 0: 
                        q.append(cost_list[pos[i]][pos[i+1]])
                        q.append(cost_list[pos[-1]][pos[0]])
                        # print(q)                        
                        ans = min(ans,(sum(q)))
                    else:
                        break                 
            else:
                chk[j] = True
                set(i+1,n)
                chk[j] = False

set(0,num_city)

print(ans)