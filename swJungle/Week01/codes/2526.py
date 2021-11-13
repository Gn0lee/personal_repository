num_list = []
for i in range(9):
    num_list.append(int(input()))
for index,value in enumerate(num_list):
    if (value == max(num_list)):
        print(value)
        print(index+1)
