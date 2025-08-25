import sys
input = sys.stdin.readline

#입력
    #1. N = 화단의 한 변의 길이
    #2. [...(N개)] (N줄): 화단의 지점당 가격

#실행
    #1. 꽃의 씨앗은 총 3개를 심고, 모든 꽃이 만개해야 한다.
    #2. 이때, 만개하는 꽃은 씨앗을 심는 곳을 기준으로 상하좌우 한칸씩 더 차지한다. (즉, 총 5칸을 차지함)
        #2-1. 즉, 꽃의 씨앗은 (1,1) ~ (N-1, N-1) 크기의 정사각형 필드에만 심어야 함. (테두리 부분은 무조건 맵 탈출)
        #2-2. 각 씨앗을 중심으로 상하좌우는 +2칸 이내에 있으면 안되며, 대각선으로는 1칸 이내에 있으면 안 된다. (즉, 상하좌우는 3칸 이상 떨어져있고, 대각선은 2칸 이상 떨어져 있어야 함)
    #3. 꽃이 만개한 이후에 각 꽃의 꽃잎 혹은 꽃술이 닿으면 안 된다.

#출력
    #1. 꽃을 심기 위한 최소 비용을 출력한다.

N = int(input())
move_lst = [(2,0), (1,0), (0,1), (0,2), (-2,0), (-1,0), (0,-1), (0,-2), (1,1), (1,-1), (-1,1), (-1,-1)]
mangae_lst = [(0,1), (0,-1), (1,0), (-1,0)]

flower_lst= []
for _ in range(N):
    input_data = list(map(int, input().rstrip().split()))
    flower_lst.append(input_data)

min_v = float('INF')
tmp = []

def check_rule(next_x, next_y):
    if len(tmp) == 0:
        return True #넣을 수 있다
    
    for tmp_x, tmp_y in tmp:
        for mx, my in move_lst:
            if next_x == tmp_x + mx and next_y == tmp_y + my:
                return False #넣을 수 없다 -> 만개했을 경우 겹침
            
    return True


def DFS(cur_x, cur_y):
    global min_v

    if len(tmp) == 3:
        total = 0

        for x, y in tmp:
            total += flower_lst[x][y]
            for mx, my in mangae_lst:
                total += flower_lst[x+mx][y+my]

        min_v = min(min_v, total)
        return True
    
    for next_x in range(1, N-1):
        for next_y in range(1, N-1):
            if visited[next_x][next_y] == True:
                continue

            ret_check = check_rule(next_x, next_y)

            if ret_check == True: #값을 넣을 수 있는 경우
                tmp.append((next_x, next_y))
                visited[next_x][next_y] = True
                DFS(next_x, next_y)
                tmp.pop(-1)
                visited[next_x][next_y] = False

            else: continue #다음 값을 넣을 수 없는 경우 -> 다음 next_x, next_y로 패스

visited = [([False] * N) for _ in range(N)]
DFS(1,1)

print(min_v)