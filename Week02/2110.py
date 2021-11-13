import sys

num_house , num_wifi = list(map(int,sys.stdin.readline().split()))
house_list = [int(sys.stdin.readline()) for _ in range(num_house)]
house_list.sort()
wifi_index_list = []
global ans
ans = 0



def wifi_search(arr,start,end,n):
    global ans
    while start <= end:
    
        mid = (start + end) //2
        first_wifi = arr[0]
        count = 1    
        for i in range(1,len(arr)):
            if arr[i] - first_wifi >= mid:
                count += 1
                first_wifi = arr[i]
        
        if count >= n:
            start = mid + 1
            ans = mid
        else:
            end = mid -1
    
wifi_search(house_list,1,house_list[-1]-house_list[0],num_wifi)
print(ans)        
        