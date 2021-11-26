import sys
input = sys.stdin.readline

n , k = map(int,input().split())

weight_list = [0]

dp = [[0] * (k+1) for _ in range(n+1) ]

for _ in range(n):
    w , v = map(int,input().split())
    
    weight_list.append([w,v])
    


for i in range(1,n+1):
    for j in range(k+1):
        if j < weight_list[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight_list[i][0]]+weight_list[i][1])


print(dp[n][k])
    