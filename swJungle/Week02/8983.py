import sys
from bisect import bisect_left,bisect_right


M,N,L = list(map(int,sys.stdin.readline().split())) # M: 사대의 수 N: 동물의 수 L: 사정거리

gun_location = list(map(int,sys.stdin.readline().split()))

animal_location = [  list(map(int,sys.stdin.readline().split()))  for _ in range(N)]
gun_location.sort()
animal_cnt = 0

for animal in animal_location:
    if animal[1] >L:
        continue
    
    min_gun = animal[0]-(L - animal[1])
    max_gun = animal[0]+(L - animal[1])
    if min_gun < 0:
        min_gun = 1
    if bisect_left(gun_location,min_gun) != bisect_right(gun_location,max_gun):
        animal_cnt += 1
            

print(animal_cnt)