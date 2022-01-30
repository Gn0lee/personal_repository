from collections import deque

def solution(places):
    answer = []

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    def chk(place):
        q = deque([])

        for j in range(5):
            for i in range(5):
                if place[j][i] == "P":
                    q.append([j,i])

        for _ in range(len(q)):    
            start_y, start_x = q.popleft()
            chk = set()
            q1 = deque([])
            chk.add((start_y,start_x))
            q1.append([start_y,start_x])

            for ___ in range(2):
                for __ in range(len(q1)):
                    now_y,now_x = q1.popleft()
                    for k in range(4):
                        next_y,next_x = now_y+dy[k],now_x+dx[k]
                        if (next_y,next_x) not in chk and 0<=next_x<5 and 0<=next_y<5 and place[next_y][next_x] == "P":
                            return False
                        elif (next_y,next_x) not in chk and 0<=next_x<5 and 0<=next_y<5 and place[next_y][next_x] == "O":
                            q1.append([next_y,next_x])
                            chk.add((next_y,next_x))
        return True

    for place in places:
        
        if chk(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))