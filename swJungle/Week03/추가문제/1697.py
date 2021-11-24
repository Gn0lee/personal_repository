from collections import deque

n , k = map(int,input().split())
time = [0] * 100001
q = deque([])
q.append(n)


while q:
    x = q.popleft()
    if x == k:
        print(time[x])
        break
    
    for nx in (x-1,x+1,2*x):
        if 0<=nx<=100000 and not time[nx]:
            time[nx] = time[x] + 1
            q.append(nx)

