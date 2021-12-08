def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i , h  in enumerate(citations):
        if i+1 <= h:
            answer = max(answer,i+1)

    return answer
