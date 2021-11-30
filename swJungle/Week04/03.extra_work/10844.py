n = int(input())

dp = [[1]*10 for _ in range(n)]

dp[0][0] = 0

if n == 1:
    print(9)
    exit(0)


for i in range(1,n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1] % 1000000000
        elif j == 9:
            dp[i][j] = dp[i-1][j-1] % 1000000000
        else:
            dp[i][j] = dp[i-1][j+1] % 1000000000 + dp[i-1][j-1] % 1000000000

result = 0

for k in range(10):
    result += dp[n-1][k] % 1000000000

print(result % 1000000000)