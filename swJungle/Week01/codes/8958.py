# import sys
# testcase = int(sys.stdin.readline())
# test_list = []
# for i in range(testcase):    
#     test_list.append(sys.stdin.readline())
# for test in test_list:
#     grade = 0
#     total_grade = 0
#     mid_grade = 0
#     for index in test:
#         if(index == "O"):
#             grade += 1
#             mid_grade += grade
#         else:
#             total_grade += mid_grade
#             mid_grade = 0
#             grade = 0
#     print(total_grade)

testcase = int(input())
test_list = []
for i in range(testcase):    
    test_list.append(input())
    
for test in test_list:
    test += "X"
    grade = 0
    total_grade = 0
    mid_grade = 0
    
    for index in test:
        if(index == "O"):
            grade += 1
            mid_grade += grade
            # total_grade += mid_grade
        else:
            total_grade += mid_grade
            mid_grade = 0
            grade = 0
    print(total_grade)