import sys
testcase = int(sys.stdin.readline())
test_list = []
for i in range(testcase):    
    test_list.append(sys.stdin.readline().strip())
for test in test_list:
    str_print = ""
    r = int(test.split()[0])
    s = test.split()[1]
    for chr in s:
        str_print += chr * r
    print(str_print)