"""
한 마을에 모험가가 N명 있다. 공포도가 X인 모함가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날수 있다.

N명의 모험가에 대한 정보가 주어졌을때 여행을 떠날 수 있는 그룹 수의 최댓값을 구하시오
ex) N=5 , 공포도 : 2 3 1 2 2

(1,2,3) , (2,2) 또한, 모든 모험가를 특정 그룹에 넣을 필요는 없다.


"""

# n = int(input())

# n_list = list(map(int,input().split()))

# n_list.sort()

# count = 0
# while n_list:
#     x = n_list[-1]
#     if len(n_list)>=x:
#         for _ in range(x):
#             n_list.pop()
#         count += 1

#     else:
#         break

# print(count)


n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i :
        result += 1
        count = 0

print(result)
