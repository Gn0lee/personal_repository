import sys
# def makeCountArray(index,counting_array):
#     if(count == length-1):
#         counting_array[index] += 1
#         return counting_array
#     return 
    


times = int(sys.stdin.readline())

given_array = list(map(lambda x : int(sys.stdin.readline()),range(times)))
counting_array = [0] * (max(given_array)+1)
print_array = [0] * len(given_array)

for i in map(lambda x: x,given_array):
    counting_array[i] += 1

for i in map(lambda x : x,range(1,len(counting_array))):
    counting_array[i] += counting_array[i-1]

for i in given_array[::-1]:
    print_array[counting_array[i]-1] = i
    counting_array[i] -= 1

for i in map(lambda x : str(print_array[x])+"\n" if x != times-1 else str(print_array[x]) ,range(times)):
    sys.stdout.write(i)