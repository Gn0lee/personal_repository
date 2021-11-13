import sys
from collections import deque
from itertools import permutations
num_city = int(sys.stdin.readline())

cost_list = [list(map(int,sys.stdin.readline().split())) for i in range(num_city)]

pos = list(map(list, permutations(range(num_city))))


ans = 10000000000

for i in permutations(range(num_city)):
    q = 0
    for j in range(num_city-1):
        if cost_list[i[j]][i[j+1]] != 0 and j < num_city -2:
            q += cost_list[i[j]][i[j+1]]
        elif cost_list[i[j]][i[j+1]] != 0 and j == num_city -2 and cost_list[i[-1]][i[0]] != 0: 
            q += cost_list[i[j]][i[j+1]]
            q += cost_list[i[-1]][i[0]]
            # print(q)                        
            ans = min(ans,q)
        else:
            break


print(ans)
