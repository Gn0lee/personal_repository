import sys
num_stick = int(input())
list_stick = [int(sys.stdin.readline()) for _ in range(num_stick)]

ans = 1

standard_stick = list_stick.pop()
while list_stick:
    
    if list_stick[-1] > standard_stick:
        standard_stick = list_stick.pop()
        ans += 1
    else:
        del list_stick[-1]

print(ans)   