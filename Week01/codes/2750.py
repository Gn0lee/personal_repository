times = int(input())
nums_list =[]
for time in range(times):
    num = int(input())
    nums_list.append(num)
nums_list.sort()
for num in nums_list:
    print(num)