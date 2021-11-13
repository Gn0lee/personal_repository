
from collections import deque

# from collections import deque
# def permu (arr,str_list):
    
#     if len(str_list) == 6:
#         print(*str_list)
#         return

#     if arr[0] in str_list:
#         del arr[0]
#         print(*arr)
#         permu(arr,str_list)    
#     else:
#         str_list.append(arr.popleft())
#         print(*arr)
#         permu(arr,str_list)
        
# permu(deque([1,2,3,4,5,6,7,8]),deque())

a = deque([1,2,3,4,5,6,7,8])

print(a.popleft())