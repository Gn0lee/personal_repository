given_str = input().split()
a = int(given_str[0])
b = int(given_str[1])

a_invert = a//100 + a%100 - a % 10 + (a%10)*100
b_invert = b//100 + b%100 - b % 10 + (b%10)*100

if (a_invert > b_invert):
    print(a_invert)
else:
    print(b_invert)