import sys
from collections import deque

def changeDirection(d,c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if c == "L":
        d = (d-1) %4
    else:
        d = (d+1) %4
    return d

dy = [-1,0,1,0]
dx = [0,1,0,-1]


def move():
    direction = 1
    time = 1
    y,x = 0,0 #start location

    visited = deque([[y,x]])
    board[y][x] = 2 #시작 지점 방문처리

    while True:

        y , x = y + dy[direction],x+dx[direction]
        if 0<=y<n and 0<=x <n and board[y][x] !=2:
            if not board[y][x] == 1: # 사과가 없을시 
                tempY,tempX = visited.popleft()
                board[tempY][tempX] = 0 # 꼬리제거
            
            board[y][x] =2 #새로운 위치 방문처리
            visited.append([y,x]) #몸통에 추가
        
            if time in times.keys():
                direction = changeDirection(direction,times[time])
            time += 1

        else:
            return time

if __name__ == "__main__":
    n = int(input())
    board = [ [0] * n for i in range(n)] ##방문하지 않은곳은 0
    k = int(input())
    for _ in range(k):
        j , i = map(int,sys.stdin.readline().split())
        board[j-1][i-1] = 1 ##사과가 있는곳은 1
    l = int(input())
    times = {}
    for _ in range(l):
        time , d = map(str,sys.stdin.readline().split())
        times[int(time)] = d ## 시간때마다 회전하도록 방향설정

    print(move())


