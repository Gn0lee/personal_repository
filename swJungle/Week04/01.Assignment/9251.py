text1 = input()
text2 = input()

dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]


for i in range(len(text1)-1,-1,-1):
    for j in range(len(text2)-1,-1,-1):
        if text1[i] == text2[j]:
            dp[i][j] = dp[i+1][j+1] + 1
        else:
            dp[i][j] = max(dp[i+1][j],dp[i][j+1])

print(dp[0][0])
