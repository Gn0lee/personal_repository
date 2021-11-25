n , k  = map(int,input().split())

money = []

for _ in range(n):
    money.append(int(input()))


count = 0

while money:
    coin = money.pop()
    
    if k == 0:
        break
    
    if k < coin:
        continue
    else:
        count += (k // coin)
        k %= coin

print(count)