import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
num_str = str(a*b*c)
for i in range(10):
    print(num_str.count(str(i)))