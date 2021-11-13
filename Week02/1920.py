import sys
n = int(input())
a = list(map(int,sys.stdin.readline().split()))
m = int(input())
ms = list(map(int,sys.stdin.readline().split()))

for i in ms:
    if i in a:
        print(1)
    else:
        print(0)