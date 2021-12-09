def solution(answers):
    answer = []
    
    students = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    modular = [5,8,10]
    scores = [0,0,0]
    
    for i in range(3):
        grade = 0
        for index , x in enumerate(answers):
            if students[i][index%modular[i]] == x:
                grade += 1
        scores[i] = grade
    
    max_score = max(scores)
    
    for i,score in enumerate(scores):
        if score == max_score:
            answer.append(i+1)
    
            
    return answer