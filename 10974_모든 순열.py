from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

tmp = []
answer = []
visited = [False] * (N+1) #index = 0 ~ N

def DFS():
    if len(tmp) == N:
        print(*tmp)
        return True
    
    for i in range(1, N+1):
        if visited[i] == False:
            visited[i] = True
            tmp.append(i)

            DFS()

            visited[i] = False
            tmp.pop(-1)

DFS()