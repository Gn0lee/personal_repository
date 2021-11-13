testcase = int(input())
num_list = []
for i in range(testcase): 
    val_str = input()
    a = int(val_str.split()[0])
    b = int(val_str.split()[1])
    num_list.append(a+b)
for num in num_list:
    print(num)
