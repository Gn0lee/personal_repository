import sys
input = sys.stdin.readline
from math import sqrt
inf = int(1e9)


n , m = map(int,input().split())

dp = [[inf]*(int(sqrt(2*n))+2) for _ in range(n+1)]

dp[1][0] = 0

stones = set() 

for _ in range(m):
    stones.add(int(input()))

for i in range(2,n+1):
    if i in stones:
        continue
    for v in range(1,int(sqrt(2*i))+1):
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1]) + 1

result = min(dp[n])

if result == inf:
    print(-1)
else:
    print(result)