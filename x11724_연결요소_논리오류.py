#반례 - https://www.acmicpc.net/board/view/130760
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
from collections import deque

max_num , line = map(int, input().rstrip().split()) #1~max_num개의 점 // line개의 간선
line_lst = [0] * line

for i in range(line):
    from_to = list(map(int, input().rstrip().split()))
    line_lst[i] = from_to

#bfs -> que
q = deque()
q.append(line_lst[0])
is_go = [True] * line #n번째 간선이 이미 들른 곳이라면 False로 표현
is_go[0] = False


def func(st, nd):
    for i in range(1, line):
        if is_go[i] == True: #해당 간선이 방문하지 않은 간선일 때
            if st in line_lst[i] or nd in line_lst[i]: #시작점과 끝점이 line_lst[i]에 하나라도 있을 떄
                is_go[i] = False
                func(line_lst[i][0],line_lst[i][1])

            else:
                if len(q) == 0:
                    q.append([line_lst[i][0], line_lst[i][1]])
                

cnt = 0
while(q):
    first, second = q.popleft()
    func(first, second)
    cnt += 1

print(cnt)