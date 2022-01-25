def solution(land):
    answer = 0
    n = len(land)
    dp = [[0]*4 for _ in range(n)]
    dp[0][0],dp[0][1],dp[0][2],dp[0][3] = land[0][0],land[0][1],land[0][2],land[0][3]
    
    for i in range(1,n):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][:j]+dp[i-1][j+1:])
    
    answer = max(dp[n-1])

    return answer