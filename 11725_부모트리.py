#https://www.acmicpc.net/board/view/134999 <- 참고해서 풀어보셈 ㅈㄴ 간결하네
#위 링크 참고해서 품
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

node = int(input().rstrip()) #노드 갯수
line_lst = [[] for i in range(node+1)] #간선 List


for i in range(node-1):
    x,y = map(int, input().rstrip().split())
    line_lst[x].append(y)
    line_lst[y].append(x)

Visited = [False] * (node+1)
output_lst = [''] * (node+1)

def DFS(point):
    Visited[point] = True

    for i in line_lst[point]:
        if Visited[i] == False: #i번쨰 인덱스가 방문하지 않을 때,
            output_lst[i] = point
            DFS(i)

DFS(1)

output_lst.pop(0)
output_lst.pop(0)
print(*output_lst)