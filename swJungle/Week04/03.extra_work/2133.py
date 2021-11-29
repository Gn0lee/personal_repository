def cal_tile(n):
    dp = [0] * 31
    dp[0] = 1
    dp[2] = 3

    for i in range(4,n+1,2):
        dp[i] = 2 * sum(dp[:i-1]) + dp[i-2]

    return dp[n]




if __name__ == "__main__":
    n = int(input())
    if n%2 == 1:
        print(0)
        exit(0)
    elif n == 2:
        print(3)
        exit(0)
    else:
        print(cal_tile(n))