from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(start, end):
    if start <= -1 or start >= w or end <= -1 or end >= h : #범위에 없을 경우
        return False
    
    if land[end][start] == 1:
        #상하좌우
        land[end][start] = 0
        DFS(start+1, end)
        DFS(start, end+1)
        DFS(start-1, end)
        DFS(start, end-1)

        #대각선
        DFS(start+1, end+1)
        DFS(start+1, end-1)
        DFS(start-1, end+1)
        DFS(start-1, end-1)
        return True
    
    return False #범위내에 있으나, 해당 지점이 바다인 경우  

while(True):
    w, h = map(int, input().rstrip().split()) #너비와 높이
    if w == 0 and h == 0:
        break

    land = [] 
    for i in range(h):
        data = list(map(int, input().rstrip().split())) #0은 바다 / 1은 땅
        land.append(data)
        #land[h-1][w-1] <- 최대 범위

    cnt = 0
    for i in range(w):
        for j in range(h):
            res = DFS(i,j)
            if res:
                cnt += 1

    print(cnt)