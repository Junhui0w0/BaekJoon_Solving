import sys
input = sys.stdin.readline

#입력
    #1. N, M -> N: 행의 크기 / M: 열의 크기
    #2. r, c, d -> r: 로봇청소기가 위치한 행의 번호 / c: 로봇청소기가 위치한 열의 번호 / d: 로봇청소기가 바라보고 있는 방향
    #3. [...(M개)] (N줄): 맵 정보

#실행
    #1. 로봇청소기가 바라보는 방향은 아래와 같이 표현할 수 있다.
        #1-1. 0=북 / 1=동 / 2=남 / 3=서
    #2. 맵 정보는 0(청소해야할 곳), 1(벽)로 구성되어 있다.
    #3. 로봇청소기가 위치한 곳(r,c)는 항상 0이다.
    #4. 로봇청소기의 동작은 아래와 같다.
        #4-1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        #4-2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우 아래와 같이 작동한다.
            #4-2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            #4-2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        #4-3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우 아래와 같이 작동한다.
            #4-3-1. 반시계 방향으로 90도 회전한다.
            #4-3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            #4-3-3. 1번으로 돌아간다.

#출력
    #1. 로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.

N, M = map(int, input().rstrip().split())
r, c, d = map(int, input().rstrip().split())
move_lst = [(0,-1), (1,0), (0,1), (-1,0)] #좌, 하, 우, 상
    #d=0=북쪽 가리킴 -> 90도 반시계회전 = 서쪽가리킴 => 좌 하 우 상 -> [0] [1] [2] [3] 순 진행
    #d=1=동쪽 가리킴 -> 90도 반시계회전 = 북쪽가리킴 => 상 좌 하 우 -> [3] [0] [1] [2] 순 진행  
    #d=2=남쪽 가리킴 -> 90도 반시계회전 = 동쪽가리킴 => 우 상 좌 하 -> [2] [3] [0] [1] 순 진행 

back_lst = [(1,0), (0,-1), (-1,0), (0,1)]
    #북, 동, 남, 서 의 반대편으로 이동
    #남, 서, 북, 동으로 이동

map_lst = []
for _ in range(N):
    input_data = list(map(int, input().rstrip().split()))
    map_lst.append(input_data)

def check_around(cur_x, cur_y):
    #현 좌표(cur_x, cur_y)를 기준으로 4방향에 청소할 곳(0)이 있는가? 를 판별하는 함수
    for dx, dy in move_lst:
        move_x, move_y = cur_x + dx , cur_y + dy

        if map_lst[move_x][move_y] == 0: #청소할 곳이 있다.
            return True
        
    return False #4방향 다 돌았는데 청소할 곳 없다.

cnt = 0
def DFS(cur_x, cur_y, direction):
    global cnt

    if map_lst[cur_x][cur_y] == 0: #현 위치 청소안함
        map_lst[cur_x][cur_y] = 2 #청소했음을 표시
        cnt += 1

    ret_check_around = check_around(cur_x, cur_y)

    if ret_check_around == False: #현 위치 주변에 청소할 수 있는 곳이 없음 -> 방향 고정 후 뒤로 1칸 이동
        back_x, back_y = cur_x + back_lst[direction][0], cur_y + back_lst[direction][1] #뒤로 이동한 좌표
        
        if map_lst[back_x][back_y] == 1: #뒤로 이동한 좌표가 벽(1)인 경우
            return 'End'
        
        else: #뒤로 이동한 곳이 0 또는 이미 청소한 곳
            ret_DFS = DFS(back_x, back_y, direction)

            if ret_DFS == 'End':
                return 'End'
            
    else: #주변을 청소할 수 있다면?
        for i in range(4): #반시계방향으로 90도 회전
            move_x, move_y = cur_x + move_lst[(((3*direction) % 4) + i )% 4][0], cur_y + move_lst[(((3*direction) % 4) + i )% 4][1]

            if map_lst[move_x][move_y] == 0: #청소할 수 있으면 추가
                ret_DFS = DFS(move_x, move_y, (direction+3-i)%4)

                if ret_DFS == 'End':
                    return 'End'

DFS(r,c,d)
print(cnt)