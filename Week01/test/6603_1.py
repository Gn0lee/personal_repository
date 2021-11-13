from collections import deque


test_list = []
while True:
    input_num = list(map(int,input().split()))
    if input_num == [0]:
        break
    else:
        del input_num[0]
        test_list.append(input_num)

# given_list = []
def recursion (level,start,length):
    if level == 6:
        print(*arr)
        return
    else:
        for i in range(start,length-6+level+1):
            arr[level] = given_list[i]
            recursion(level+1,i+1,length)

for test in test_list:
    given_list = [ j for j in test]
    arr = [0] * 6
    recursion(0,0,len(given_list))
    print()