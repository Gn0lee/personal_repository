import sys
from bisect import bisect_left,bisect_right


M,N,L = list(map(int,sys.stdin.readline().split())) # M: 사대의 수 N: 동물의 수 L: 사정거리

gun_location = list(map(int,sys.stdin.readline().split()))

animal_location = [ [False] + list(map(int,sys.stdin.readline().split()))  for _ in range(N)]

animal_cnt = 0

while gun_location:
    gun = gun_location.pop()
    for i in range(N):
        if not animal_location[i][0] and (abs(animal_location[i][1]-gun)+animal_location[i][2]) <= L:
            animal_cnt += 1
            animal_location[i][0] = True

print(animal_cnt)