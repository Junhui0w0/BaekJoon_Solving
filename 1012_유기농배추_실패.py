from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(10**6)

move_lst = [(-1,0), (1,0), (0,1), (0,-1)]

def func(x,y): #x,y는 배추가 심어진 좌표 // lst = ground_lst
    global cnt

    # total_lst = []
    # for move_x , move_y in move_lst:
    #     if 0<= x + move_x <= w-1 and 0 <= y + move_y <= h-1:
    #         total_lst.append(ground_lst[x+move_x][y+move_y])

    # if sum(total_lst) == 0:
    #     cnt += 1

    if(0<= x <= h-1 and 0<= y <= w-1):
        if ground_lst[x][y] == 0: #배추가 없는 땅
            return 0

        elif ground_lst[x][y] == 1: #배추가 있는 땅
            ground_lst[x][y] = 0 #갔음을 표시
            
            total_lst = []
            for move_x , move_y in move_lst:
                if 0<= x + move_x <= h-1 and 0 <= y + move_y <= w-1:
                    total_lst.append(ground_lst[x+move_x][y+move_y])
                    
            if sum(total_lst) == 0:
                cnt += 1

            func(x-1,y)
            func(x+1,y)
            func(x,y-1)
            func(x,y+1)

    else:
        return 0

        #for i in range(4):
            # nx = x + dx[i]
            # ny = y + dy[i]

            # if(0 <= nx <= w-1 and 0 <= ny <= h-1):
                



test_case = int(stdin.readline().rstrip()) #테스트케이스 갯수

ans = ''
for _ in range(test_case):
    cnt = 0
    w, h, baechu = list(map(int, stdin.readline().rstrip().split())) #가로, 세로, 배추 갯수
    ground_lst = [[0] * w for _ in range(h)]

    baechu_pos = []
    for __ in range(baechu):
        x, y = map(int, stdin.readline().rstrip().split())
        ground_lst[y][x] = 1
        baechu_pos.append([y,x])
        
    for first, second in baechu_pos:
        func(first, second)

    ans += str(cnt) + '\n'

print(ans)