import sys
testcase = int(sys.stdin.readline())
test_list = []
for i in range(testcase):
    
    test_list.append(int(sys.stdin.readline()))

def check_prime_num(x):
    for i in range(2,x):
        if(x%i == 0):
            return False
    return True
print(test_list)
for test in test_list:

    half_test = test//2
    while half_test:
        if (check_prime_num(half_test) & check_prime_num(test-half_test)):
            print("{} {}".format(half_test, test-half_test))
            break
        else:
            half_test -= 1

