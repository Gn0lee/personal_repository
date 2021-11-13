from itertools import combinations
import sys

test_list = []

while True:
    input_num = list(map(int,input().split()))
    if input_num == [0]:
        break
    else:
        del input_num[0]
        test_list.append(input_num)


for test in test_list:
    for case in combinations(test,6):
        print(*case)
    print()
