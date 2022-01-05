def solution(triangle):
    answer = 0
    n = len(triangle)
    
    dp = [[0] * i for i in range(1,n+1)]
    dp[0][0] = triangle[0][0]
    
    for j in range(1,n):
        for k in range(j+1):
            if k == 0:
                dp[j][k] = dp[j-1][k] + triangle[j][k]
            elif k == j:
                dp[j][k] = dp[j-1][k-1] + triangle[j][k]
            else:
                dp[j][k] = max(dp[j-1][k-1],dp[j-1][k]) + triangle[j][k]
    
    answer = max(dp[n-1])
    return answer