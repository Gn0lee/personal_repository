import sys
input = sys.stdin.readline
inf  = int(1e9)
n,k = map(int,input().split())

coins = []
dp = [inf] *(k+1)
dp[0] = 0

for _ in range(n):
    coins.append(int(input()))

coins = list(set(coins))

for i in coins:
    for j in range(i,k+1):
        if dp[j-i] != inf:
            dp[j] = min(dp[j],dp[j-i]+1)

if dp[k] == inf:
    print(-1)
else:
    print(dp[k])
