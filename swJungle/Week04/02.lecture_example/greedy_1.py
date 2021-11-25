"""
 - 1이 될때까지 - 

어떠한 수 N이 1이 될때까지 2가지 연산을 반복적으로 수행하려 한다.
1. N-1
2. N을 K로 나눈다

ex) 17,4 : 17 -> 16 -> 4 -> 1

과정을 수행하는 최소 횟수를 구하시오
"""

"""
#나의 풀이
n ,k = map(int,input().split())

count = 0

x = n
count = 0
while n != 1:
    if n % k ==0:
        n = n // k
        count += 1
    else:
        if n > k:
            count += n%k
            n -= (n%k)
        else:
            count += n-1
            n = 1
print(count)
#아래는 나동빈 풀이
"""

n,k = map(int,input().split())

result = 0

while True:
    target = (n //k) *k
    result += n - target
    n = target

    if n<k:
        break

    result += 1
    n //= k

result += n-1
print(result)


