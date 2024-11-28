from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split()) #가로 / 세로 / 높이

tomato_field = []
is_tomato = deque()

for i in range(N*H):
    input_data = list(map(int, input().rstrip().split())) 
    tomato_field.append(input_data)
    
    for j in range(M):
        if input_data[j] == 1:
            is_tomato.append((i,j))


move_lst = [(-1,0), (1,0), (0,1), (0,-1)]
move_h_lst = [-N, N]

while(is_tomato): #BFS 형식 -> FIFO
    x, y = is_tomato.popleft()

    for dx, dy in move_lst: #상하좌우 검사
        if x + dx <= -1 or x + dx >= (N*H) or y + dy <= -1 or y + dy >= M:
            continue

        if x // N == (x+dx) // N: #동일한 차원에 있는가에 대한 검사
            if tomato_field[x+dx][y+dy] == 0:
                tomato_field[x+dx][y+dy] = tomato_field[x][y] + 1
                is_tomato.append((x+dx, y+dy))

    for hx in move_h_lst:
        if hx + x <= -1 or hx + x >= N*H:
            continue

        if tomato_field[x+hx][y] == 0:
            tomato_field[x+hx][y] = tomato_field[x][y] + 1
            is_tomato.append((x+hx, y))

ans = False
max_v = -2
for data in tomato_field:
    if 0 in data:
        ans = True
        break

    max_v = max(max_v, max(data))

if ans == True:
    print(-1)
else:
    print(max_v-1)

# for data in tomato_field:
#     print(data, end='\n')