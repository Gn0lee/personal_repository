import sys

times = int(sys.stdin.readline())
# max = 1
given_array = []
counting_array = []
print_array=[]
for i in range(times):
    num = int(sys.stdin.readline())
    given_array.append(num)
    # if(num > max):
    #     max = num
# for i in range(max(given_array)+1):
#     counting_array.append(0)
# for i in given_array:
#     print_array.append(0)
counting_array = [0] * (max(given_array)+1)
print_array = [0] * len(given_array)
for i in given_array:
    counting_array[i] += 1
for i in range(1,len(counting_array)):
    counting_array[i] += counting_array[i-1]
for i in given_array:
    print_array[counting_array[i]-1] = i
    counting_array[i] -= 1


for i in range(times):
    sys.stdout.write(str(print_array[i])+"\n")
