"""
각자리가 0~9로만 이루어진 문자열이 주어졌을때 왼쪽부터 오른쪽으로 하니씩 모든 숫자를 확인하면 숫자 사이에 곱하기 또는 더하기 연산자를 넣어 가장큰수를 구하려한다.
ex) 02984 -> 0+2*9*8*4 모든 연산은 왼쪽에서 부터 차례대로 이루어진다.

"""
"""
나의 풀이

s = list(map(int,input()))

result = [0]*20
result[0] = s[0]

for i in range(1,len(s)):
    if s[i] == 0 or s[i] == 1 or result[i-1] == 0 or result[i-1] == 1:
        result[i] = result[i-1] + s[i]
    else:
        result[i] = result[i-1] * s[i]

print(result[len(s)-1])

아래는 나동빈 풀이

"""

data = input()

result = int(data[0])

for i in range(1,len(data)):
    num = data[i]

    if num<=1 or result <=1:
        result += num
    else:
        result *= num

print(result)
