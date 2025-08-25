from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

tmp = []
def DFS(index):
    if len(tmp) == M:
        print(*tmp)
        return True
    
    for i in range(index, N+1): #index ~ N
        tmp.append(i)
        
        DFS(i+1)

        tmp.pop(-1)

DFS(1)