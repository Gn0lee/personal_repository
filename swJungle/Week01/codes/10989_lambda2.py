import sys
def makeCountArray(index):    
    counting_array[index] += 1      
    return counting_array
def sumCountArray(index):
    counting_array[index] += counting_array[index-1]
    return counting_array 
def makePrintArray(index):
    print_array[counting_array[index]-1] = index
    counting_array[index] -= 1
    return print_array   

def printArray(index,times):
    if index != times-1:
        return str(print_array[index])+"\n"
    else:
        return str(print_array[index])

times = int(sys.stdin.readline())

given_array = list(map(lambda x : int(sys.stdin.readline()),range(times)))
counting_array = [0] * 10001
print_array = [0] * len(given_array)

list(map(lambda x: makeCountArray(x),given_array))[0]
# print(counting_array)
list(map(lambda x : sumCountArray(x),range(1,len(counting_array))))[0]
# print(counting_array)    
list(map(lambda x : makePrintArray(x),given_array[::-1]))[0]
# print(print_array)
for i in map(lambda x : printArray(x,times),range(times)):
    sys.stdout.write(i)