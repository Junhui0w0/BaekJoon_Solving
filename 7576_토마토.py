from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().rstrip().split()) #가로 / 세로 입력
tomato_field = deque()
is_tomato = deque()

for i in range(N): #1-1) 입력받으면서 토마토가 있는 위치(1)를 찾아낼 것인지 ?
    input_data = list(map(int, input().rstrip().split()))
    tomato_field.append(input_data)
    
    for v in range(M):
        if input_data[v] == 1:
            is_tomato.append((i,v))

# print(tomato_field)
# print(is_tomato)
move_lst = [(-1,0), (1,0), (0,1), (0,-1)]

#BFS 형식으로 해결 -> QUE / FIFO
while(is_tomato):
    x, y = is_tomato.popleft() #토마토가 있는 위치 x,y에 저장

    for dx, dy in move_lst:
        if x + dx <= -1 or x + dx >= N or y + dy <= -1 or y + dy >= M:
            continue

        if tomato_field[x+dx][y+dy] == 0:
            tomato_field[x+dx][y+dy] = tomato_field[x][y] + 1
            is_tomato.append((x+dx, y+dy))

max_data = -2
temp = False
for data in tomato_field:
    if 0 in data:
        temp = True
        break
    
    max_data = max(max_data, max(data))

if temp != True:
    print(max_data-1)
else:
    print(-1)