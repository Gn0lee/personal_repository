import sys
input = sys.stdin.readline
from collections import deque


for _ in range(int(input())):
    n = int(input())
    grade = []

    for __ in range(n):
        a , b = map(int,input().split())

        grade.append([a,b])

    grade.sort()

    cnt = 1

    max = grade[0][1]

    for s ,e in grade[1:]:
        if e <= max:
            cnt +=1
            max = e
        else:
            continue

    print(cnt)

