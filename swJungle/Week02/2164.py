from collections import deque

N = int(input())
N_list = deque(range(1,N+1))

while len(N_list) >1 :
    N_list.popleft()
    N_list.rotate(-1)

print(N_list[0])