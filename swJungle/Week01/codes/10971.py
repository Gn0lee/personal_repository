import sys
from collections import deque

num_city = int(sys.stdin.readline())

cost_list = [list(map(int,sys.stdin.readline().split())) for i in range(num_city)]
chk = [False] * num_city
cost_case = []
def bfs (i):
    case_cost = 0
    q = [i]
    while q:
       ci =  q.pop()
       for ni in range(num_city):
            if chk[ni] == False and cost_list[ci][ni] and ci != ni > 0:
                chk[ni] = True
                case_cost += cost_list[ci][ni]
                q.append(ni)
    return case_cost 
cost = 0
mxc = 0
for i in range(num_city):
    for j in range(num_city):
        if cost_list[i][j] > 0 and chk[j] == False:
            chk[j] = True
            cost += cost_list[i][j]
            cost += bfs(j)
            
            mxc = max(mxc,cost)
    mxc = max(mxc,cost)
    

print(mxc)