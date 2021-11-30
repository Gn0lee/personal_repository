import sys
input = sys.stdin.readline

n = int(input())

dp = [[0]* __ for __ in range(1,n+1)]

triangle = []

for _ in range(n):
    triangle.append(list(map(int,input().split())))

dp[0][0] = triangle[0][0]

for index1,x in enumerate(triangle):
    if index1 == 0:
        continue
    for index2, current in enumerate(x):
        if index2 == 0:
            dp[index1][index2] = dp[index1-1][index2] + current
        elif index2 == index1:
            dp[index1][index2] = dp[index1-1][index2-1] + current
        else:
            dp[index1][index2] = max(dp[index1-1][index2-1],dp[index1-1][index2]) + current

print(max(dp[n-1]))