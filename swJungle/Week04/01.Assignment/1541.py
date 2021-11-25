from functools import reduce

a = input()

b = a.split(sep="-")

for i,l in enumerate(b):
    x = list(map(int,l.split("+")))
    b[i] = sum(x)

z = reduce(lambda x , y : x - y ,b)
# print(b)
print(z)