# def solution(n, money):
#     answer = 0
#     dp = [[0] * (n+1) for _ in range(len(money))]
    
#     for i in range(len(money)):
#         dp[i][money[i]] = 1

#     for j in range(1,n+1):
#         for index,k in enumerate(money):
#             if j - k < 1:
#                 continue
#             else:
#                 tmp = 0
#                 for l in range(index,len(money)):
#                     tmp += dp[l][j-k]
#                 dp[index][j] = tmp % 1000000007
                
    
#     # print(*dp,sep="\n")

#     for m in range(len(money)):
#         answer = (dp[m][n] + answer) % 1000000007
            
        
    
#     return answer % 1000000007

# print(solution(10,[1,2,5]))

# def solution(n, money):
#     answer = 0
#     dp = [[0] * (len(money)) for _ in range(n+1)]
#     tmp = [0] * (n+1)
    
#     for i,m in enumerate(money):
#         dp[m][i] = 1

#     tmp[1] = sum(dp[1]) 
#     # print(*dp,sep="\n") 
#     # print()

#     for j in range(1,n+1):
#         for k, l in enumerate(money):
#             if j - l < 1:
#                 continue
#             else:
#                 dp[j][k] = sum(dp[j-l][k:])% 1000000007


#     # print(*dp,sep="\n")       
        
    
#     return sum(dp[n])% 1000000007

# print(solution(5,[1,2,5]))

# def solution(n, money):
#     dp = [[0] * (len(money)) for _ in range(n+1)]
#     tmp = [0] * (n+1)
    
#     for i,m in enumerate(money):
#         dp[m][i] = 1

#     tmp[1] = sum(dp[1]) 
#     # print(*dp,sep="\n") 
#     # print()

#     for j in range(1,n+1):
#         for k, l in enumerate(money):
#             if j - l < 1:
#                 continue
#             else:
#                 dp[j][k] = sum(dp[j-l][k:])% 1000000007


#     # print(*dp,sep="\n")       
        
    
#     return sum(dp[n])% 1000000007

# print(solution(11,[1,2,5]))
from collections import deque

def solution(n, money):
    dp = [0] * (n+1)
    money = deque(sorted(money,reverse=True))
    max_money = money.popleft()

    for i in range(max_money,n+1,max_money):
        dp[i] = 1 

    while money:
        now = money.popleft()
        dp[now] = 1
        for j in range(now+1,n+1):
            dp[j] += dp[j-now] % 1000000007        

    return dp[n] % 1000000007

print(solution(11,[1,2,5]))

def solution(n, money):
    dp = [0] * (n+1)
    money.sort()
    max_money = money.pop()

    for i in range(max_money,n+1,max_money):
        dp[i] = 1 

    while money:
        now = money.pop()
        dp[now] = 1
        for j in range(now+1,n+1):
            dp[j] += dp[j-now] % 1000000007        

    return dp[n] % 1000000007