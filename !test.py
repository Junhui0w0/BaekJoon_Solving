
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

node = int(input())  # 노드 갯수
start, end = map(int, input().rstrip().split())  # start는 end의 몇 촌?

time = int(input())  # 라인 입력받을 횟수
line_lst = []
Visited = [False] * time  # 방문했는지?

for i in range(time):
    input_data = list(map(int, input().rstrip().split()))
    line_lst.append(input_data)

def DFS(point):
    global cnt
    if point == end:
        return cnt

    for i in range(time):
        if point in line_lst[i]:
            next_point = sum(line_lst[i]) - point  # 다음 탐색할 노드
            if not Visited[i]:
                Visited[i] = True
                cnt += 1
                result = DFS(next_point)
                if result != -1:
                    return result
                cnt -= 1  # 탐색 실패 시 카운트 복구

    return -1  # 모든 경로를 탐색한 후 종료 조건을 만족하지 않을 때

cnt = 0
print(DFS(start))
