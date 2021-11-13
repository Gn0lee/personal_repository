n_x_list = input().split()
x = int(n_x_list[1])
a_list = input().split()
answer = ""
for a in a_list:
    if(int(a) < x):
        answer += (a+" ")
print(answer) 
    