def heapify(arr,n,i):
    mother = i
    left_node = 2 * i +1
    right_node = 2* i + 2
    if (left_node<n and arr[left_node] > arr[mother]):
        mother = left_node
    if(right_node<n and arr[right_node] > arr[mother]):
        mother = right_node
    if(mother != i): 
        arr[i] , arr[mother] = arr[mother] , arr[i]
        heapify(arr,n,mother)

def heapSort(arr):
    n = len(arr)
    for i in range(n,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
import sys

times = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for i in range(times)]
    
heapSort(arr)
print(*arr, sep="\n")