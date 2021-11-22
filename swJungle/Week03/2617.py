import sys
input = sys.stdin.readline

n , m = map(int,input().split())

marbles = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    big , small = map(int,input().split())
    marbles[big][small] = 1

for a in range(1,n+1):
    marbles[a][a] = 0

for k in range(1,n+1):
    for j in range(1,n+1):
        for i in range(1,n+1):
            if marbles[j][k] == 1 and marbles[k][i] == 1:
                marbles[j][i] = 1

ans = 0

for j in range(1,n+1):
    bigger_marbles = 0
    smaller_marbles = 0
    for i in range(1,n+1):
        if i==j:
            continue
        elif marbles[j][i] == 1:
            bigger_marbles +=1
        elif marbles[i][j] == 1:
            smaller_marbles += 1
    if bigger_marbles > n//2 or smaller_marbles > n//2:
        ans += 1

print(ans)