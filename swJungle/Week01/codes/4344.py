import sys
testcase = int(sys.stdin.readline())
test_list = []
for i in range(testcase):    
    test_list.append(sys.stdin.readline())
for test in test_list:
    total = 0
    upper_avg = 0
    num_list = test.split()
    del num_list[0]
    for i in num_list:
        total += int(i)
    avg = total / (len(num_list))
    # print(total)
    # print(len(num_list))
    # print(avg)
    for i in num_list:
        if(int(i)>avg):
            upper_avg +=1
    print(format(upper_avg/len(num_list)*100,".3f")+"%")