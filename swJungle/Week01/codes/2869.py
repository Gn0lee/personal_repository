given_str = input().split()
a = int(given_str[0])
b = int(given_str[1])
v = int(given_str[2])

if(v<=a):
    print(1)
else:
    print(((v-a-1)//(a-b))+2)