from collections import deque


n , m ,v= map(int,input().split())

board = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a , b = map(int, input().split())
    board[a][b] , board[b][a] = 1,1

chk = [False] * (n+1)
chk2 = [False] * (n+1)

def bfs(v):
    
    chk[v] = True
    
    q = deque([v])
    while q:
        x = q.popleft()
        print(x, end=" ")
        for i in range(1,n+1):
            if board[x][i] == 1 and not chk[i]:
                q.append(i)
                chk[i] = True

def dfs(v):
    
    chk2[v] = True
    print(v,end=" ")
    for i in range(1,n+1):
        if not chk2[i] and board[v][i] ==1:
            dfs(i)

dfs(v)
print()
bfs(v)