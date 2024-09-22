from collections import deque
import sys
#sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def func(pos_x, pos_y):
    #ground_lst[pos_y][pos_x] 해야 오류 안남
    #pos_x의 범위는 0 ~ m-1 // pos_y의 범위는 0 ~ n-1
    if pos_x <= -1 or pos_x >= m or pos_y <= -1 or pos_y >= n:
        return False
    
    if ground_lst[pos_y][pos_x] == 1:
        ground_lst[pos_y][pos_x] = 0
        func(pos_x +1, pos_y)
        func(pos_x -1, pos_y)
        func(pos_x, pos_y +1)
        func(pos_x, pos_y -1)
        return True
    
    return False


test_case = int(input().rstrip()) #시행 횟수

for _ in range(test_case):
    m,n,k = map(int, input().rstrip().split()) #가로, 세로, 배추 갯수
    baechu_lst = []
    ground_lst = [([0]*m) for zero in range(n)] #배추를 재배할 밭

    for __ in range(k):
        x, y = map(int, input().rstrip().split()) #배추가 심어져있는 좌표
        ground_lst[y][x] = 1

    total = 0
    for i in range(m):
        for j in range(n):
            if func(i,j) == True:
                total += 1
    
    print(total)