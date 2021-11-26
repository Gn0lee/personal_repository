import sys
input = sys.stdin.readline

n = int(input())

time_list = []

for _ in range(n):
    a , b = map(int,input().split())
    time_list.append([a,b])

time_list.sort(key=lambda x : (x[1],x[0]))

start , end = time_list.pop(0)

count = 1
for s , e in time_list:
    if s >= end:
        end = e
        count += 1

print(count)