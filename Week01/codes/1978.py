import sys
testcase = int(sys.stdin.readline())
test_list = sys.stdin.readline().split()
prime_ea = 0
def check_prime_num(x):
    if(x == 1):
        return False
    else:
        for i in range(2,x):
            if(x%i == 0):
                return False
        return True

for test in test_list:
    if(check_prime_num(int(test))):
        prime_ea += 1
print(prime_ea)