import sys

n = int(input())
num_list = list(map(int,sys.stdin.readline().split()))


ans = 0
cnt = 0
while True:
    
    beforeswp = list(map(lambda x : x ,num_list))
    
    i = 0
    while True:
        if i == n-1:
            break
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1],num_list[i]
            ans += 1
        i += 1
    cnt += 1
    if beforeswp == num_list:
        break
            

        

print(cnt)
print(ans)