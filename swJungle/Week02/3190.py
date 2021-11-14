import sys
from collections import deque

apples = [[False]*100 for _ in range(100)]
N = int(input())
K = int(input())

for _ in range(K):
    j , i = map(int,sys.stdin.readline().split())
    apples[j-1][i-1] = True


L = int(input())
rotate = [0] * 10001
for _ in range(L):
    time , direction = sys.stdin.readline().split()
    rotate[int(time)] = direction

T = 1
tail = [0,-1]
head = [0,0]

first_info = [head,tail]
q = deque(first_info)
while q:
    cr_head = q[0]
    before_head = q[1]
    cr_tail = q.pop()
    n_head = [0,0]

    if rotate[T-1] ==0:
        if before_head[0] == cr_head[0] and cr_head[1] > before_head[1]: # before_head왼  h오
            n_head = [cr_head[0],cr_head[1]+1]    
        elif before_head[0] == cr_head[0] and cr_head[1] < before_head[1]: #before_head오 h왼
            n_head = [cr_head[0],cr_head[1]-1]
        elif before_head[1] == cr_head[1] and cr_head[0] < before_head[0]:  #before_head위 h아
            n_head = [cr_head[0]+1,cr_head[1]]  
        else:                                                       #before_head아 h위
            n_head = [cr_head[0]-1,cr_head[1]]
        if  not(0<=n_head[0]<N) or not(0<=n_head[0]<N):
            break
        if n_head in q:
            break
    elif rotate[T-1] == "D": ##오른쪽 회전
        if before_head[0] == cr_head[0] and cr_head[1] > before_head[1]: # before_head왼  h오
            n_head = [cr_head[0]+1,cr_head[1]]    
        elif before_head[0] == cr_head[0] and cr_head[1] < before_head[1]: #before_head오 h왼
            n_head = [cr_head[0]-1,cr_head[1]]
        elif before_head[1] == cr_head[1] and cr_head[0] < before_head[0]:  #before_head위 h아
            n_head = [cr_head[0],cr_head[1]-1]  
        else:                                                       #before_head아 h위
            n_head = [cr_head[0],cr_head[1]+1]
        if  not(0<=n_head[0]<N) or not(0<=n_head[0]<N):
            break
        if n_head in q:
            break
    else:                ##왼쪽회전
        if before_head[0] == cr_head[0] and cr_head[1] > before_head[1]: # before_head왼  h오
            n_head = [cr_head[0]-1,cr_head[1]]    
        elif before_head[0] == cr_head[0] and cr_head[1] < before_head[1]: #before_head오 h왼
            n_head = [cr_head[0]+1,cr_head[1]]
        elif before_head[1] == cr_head[1] and cr_head[0] < before_head[0]:  #before_head위 h아
            n_head = [cr_head[0],cr_head[1]-1]  
        else:                                                       #before_head아 h위
            n_head = [cr_head[0],cr_head[1]+1]
        if  not(0<=n_head[0]<N) or not(0<=n_head[0]<N):
            break
        if n_head in q:
            break
    
    if apples[n_head[0]][n_head[1]]:
        q.append(cr_tail)
        apples[n_head[0]][n_head[1]] = False
    
    q.appendleft(n_head)
    T += 1
    
    
    
print(T)



