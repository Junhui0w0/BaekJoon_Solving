from collections import deque
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m = map(int, input().rstrip().split()) #lst[0][0] ~ lst[n-1][m-1]
board_lst = []
for i in range(n):
    input_data = list(map(int, input().rstrip()))
    board_lst.append(input_data)

#print(board_lst) #디버깅

#따저야할 조건
#1. start와 end값이 지정된 board 범위를 넘어가는가?
#2. cnt가 (움직인거리)가 최소가 되도록 하였는가?
#3. 보드 좌표의 요소가 1인 경우에만 움직일 수 있음
#4. 갈 수 있는 길을 찾으면, 방문하고 방문한 좌표의 요소 값을 지금껏 이동한 거리로 둠
    #(다시 방문할 수 있는 문제점 해결) -> BFS
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def BFS(start, end):
    d = deque()
    d.append((start, end))

    while(d):
        x, y = d.popleft() #BFS는 선입선출(FIFO)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m: #지정 보드 넘어갈 때
                continue
            
            if board_lst[nx][ny] == 0: #해당 좌표가 벽이라면
                continue
            
            if board_lst[nx][ny] == 1: #해당 좌표가 한번도 방문하지 않은 곳이라면,
                board_lst[nx][ny] = board_lst[x][y] + 1 #직전 좌표의 +1
                d.append((nx, ny))
                
    return board_lst[n-1][m-1]

print(BFS(0,0))
