def solution(brown, yellow):
    from math import sqrt
    
    answer = []
    
    for a in range(int(sqrt(yellow)),yellow+1):
        if yellow % a != 0:
            continue
        else:
            b = yellow // a
            if b <= a and 2*(a+b+2) == brown:
                answer.append(a+2)
                answer.append(b+2)
                break
    
    return answer