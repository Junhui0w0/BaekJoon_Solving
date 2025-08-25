import sys
input = sys.stdin.readline

#입력
    #1. [...] (5x5크기의 배열): 맵 정보 (0: 빈칸 / 1: 사과 / -1: 장애물)
    #2. r, c -> r: 학생이 위치한 행의 번호 / c: 학생이 위치한 열의 번호

#실행
    #1. 학생은 r,c에서 시작하며, 상하좌우 중 한 방향으로 한 칸 이동할 수 있다.
        #1-1. 이때, 이동하고 원래 있던 자리는 장애물(-1)로 변경된다.

#출력
    #1. 3번 이하의 이동으로 사과를 2개 이상 먹을 수 있다면 1을 출력하고, 그렇지 않으면 0을 출력한다.

data_lst = []
for _ in range(5):
    input_data = list(map(int, input().rstrip().split()))
    data_lst.append(input_data)

r, c = map(int, input().rstrip().split())

cnt = 0 #움직이면서 먹은 사과 갯수
move_lst = [(-1, 0), (1,0), (0,1), (0,-1)] #가능한 움직임

def DFS(cur_x, cur_y, move):
    global cnt

    if move > 3: #움직인 횟수가 3 초과면 fail
        return False
    
    if cnt >= 2:
        return True

    for dx, dy in move_lst:
        move_x, move_y = dx + cur_x, dy + cur_y

        if not(0 <= move_x <= 4 and 0 <= move_y <= 4): #맵 탈출
            continue

        if data_lst[move_x][move_y] == -1: #장애물이면 패스
            continue

        elif data_lst[move_x][move_y] == 1: #사과인 경우
            cnt += 1
            data_lst[move_x][move_y] = -1
            
            ret = DFS(move_x, move_y, move+1)
            if ret:
                return ret

            cnt -= 1
            data_lst[move_x][move_y] = 1

        elif data_lst[move_x][move_y] == 0: #빈칸
            data_lst[move_x][move_y] = -1

            ret = DFS(move_x, move_y, move+1)
            if ret:
                return ret
            
            data_lst[move_x][move_y] = 0

    return False

data_lst[r][c] = -1 #현 위치 출발 -> 현 위치는 장애물로 표시
ret = DFS(r, c, 0)
if ret:
    print(1)

else:
    print(0)