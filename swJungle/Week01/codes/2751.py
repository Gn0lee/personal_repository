import sys

times = int(sys.stdin.readline())
array = [int(sys.stdin.readline().strip()) for i in range(times)]
    

def quick_sort1(array, start, end):
    # base case
    if start >= end: # 원소가 1개인 경우 종료
        return
	
    # recursive case
    pivot = start # 피벗은 첫 번째 원소로 설정
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort1(array, start, right - 1)
    quick_sort1(array, right + 1, end)

# def quick_sort2(array):
#     if (len(array) <= 1):
#         return array
#     pivot = array[0]
#     tail = array[1:]
#     left_side = list(filter(lambda x : x <= pivot,tail))
#     right_side = list(filter(lambda x : x > pivot,tail))
#     return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

quick_sort1(array,0,times-1)
print(*array, sep="\n")
