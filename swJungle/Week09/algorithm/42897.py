def solution(money):
    answer = 0
    n = len(money)
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    dp1[0] , dp1[1] = money[0] , max(money[0],money[1])
    dp2[0] , dp2[1] = 0 , money[1]
    
    for i in range(2,n):
        if i != n-1:
            dp1[i] = max(dp1[i-1],dp1[i-2] + money[i])
            dp2[i] = max(dp2[i-1],dp2[i-2] + money[i])
        else:
            dp1[i] = dp1[i-1]
            dp2[i] = max(dp2[i-1],dp2[i-2] + money[i])
        
    answer = max(dp1[n-1],dp2[n-1]) 
    return answer