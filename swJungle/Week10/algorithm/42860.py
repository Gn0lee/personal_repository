#https://bellog.tistory.com/152

def solution(name):
    answer = 0

    n = len(name)
    times = n

    for i in name:
        if ord(i) == 65:
            continue
        elif ord(i) > 78:
            answer += 91 - ord(i)
        else:
            answer += ord(i) - 65
    
    for j in range(n):
        next_A = j + 1

        while next_A<n and name[next_A] == "A":
            next_A += 1

        times = min(times,j+j+n-next_A)

    answer += times

    return answer

print(solution("JEROEN"))

# name = "JAN"
# answer = 0
# to_fixed = 0
# for i in name:
#         if ord(i) == 65:
#             continue
#         elif ord(i) > 78:
#             answer += 91 - ord(i)
#             to_fixed += 1
#         else:
#             answer += ord(i) - 65
#             to_fixed += 1