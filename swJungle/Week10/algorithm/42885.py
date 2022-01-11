from bisect import bisect_right

def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)

    under_200 = bisect_right(people,200)
  
    answer += n-under_200

    left , right = 0, under_200-1
    while left <= right:
        if left == right:
            answer += 1
            break
        elif people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            answer += 1
            right -= 1 
    
    return answer
