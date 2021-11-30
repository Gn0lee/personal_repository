import sys
input = sys.stdin.readline

n = int(input())

line = []

for _ in range(n):
    a , b = map(int,input().split())
    line.append([a,b])

line.sort(key=lambda x: x[0])

dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i],dp[j]+1)

x = max(dp)

print(n-x)