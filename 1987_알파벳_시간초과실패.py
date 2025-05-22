from collections import deque
import sys
input = sys.stdin.readline

R,C = map(int, input().rstrip().split()) # 0~R-1 행 // 0~C-1 열

board = []
# is_visited = []
for _ in range(R):
    input_data = list(input().rstrip())
    board.append(input_data)

    # is_visited.append([-1] * C)

# print(board)
# print(is_visited)

visited = set()
max_cnt = -1
#1. 우선 4방향으로 진행 (-1,0) (1,0), (0,1), (0,-1)
#2. 맵 탈출 고려
#3. 동일한 문자가 있는가? -> set 활용해서
def DFS(x,y, cnt):
    global max_cnt

    #현 좌표가 맵 탈출했는가?
    if x <= -1 or x >= R or y <= -1 or y >= C:
        return False 
    
    #현 좌표에 있는 문자가 이미 방문한 곳인가?
    alphabet = board[x][y]

    if alphabet in visited:
        return False
    else: 
        visited.add(alphabet)

    #4방향 진행
    for _ in range(4):
        DFS(x-1, y, cnt+1)
        DFS(x+1, y, cnt+1)
        DFS(x, y-1, cnt+1)
        DFS(x, y+1, cnt+1)

    visited.remove(alphabet)
    if cnt > max_cnt:
        max_cnt = cnt

DFS(0,0,1)
print(max_cnt)