number = 8
sorted = [0] * 8
arr1 =[7,6,5,8,3,5,9,1]
def merge(arr,start,middle,end):
    i = start
    j = middle +1
    k = start
    while (i <= middle and j <= end):
        if arr[i] <= arr[j]:
            sorted[k] = arr[i]
            i += 1
        else:
            sorted[k] = arr[j]
            j += 1
        k += 1
        if i > middle:
            while j == end:
                sorted[k] = arr[j]
                j +=1
        else:
            while i == middle:
                sorted[k] = arr[i]
                i+=1
        
    for x in range(start,end+1):
        arr[x] = sorted[x]

def mergeSort(arr,start,end):
    if start < end:
        mid = (start + end ) // 2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid,end)

mergeSort(arr1,0,7)
print(*arr1)