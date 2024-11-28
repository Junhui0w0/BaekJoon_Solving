from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) #데이터 갯수
time_lst = []

for i in range(n):
    input_data = list(map(int, input().rstrip().split()))
    time_lst.append(input_data)

# #DFS로 풀면 시간초과 -> 불필요한 곳까지 전부 탐색해서 그런듯
# time_lst.sort()

# max_v = -1
# def DFS(start, end, start_index, cnt):
#     global max_v
#     for i in range(start_index, n):
#         if visited[i] == True:
#             continue

#         if time_lst[i][0] >= end:
#             visited[i] = True
#             cnt += 1
#             max_v = max(max_v, cnt)
#             DFS(end, time_lst[i][1], start_index, cnt)
#             visited[i] = False
#             cnt -= 1

    

# for i in range(n):
#     if max_v >= n - i:
#         break

#     visited = [False] * n
#     cnt = 1
#     DFS(time_lst[i][0], time_lst[i][1], i, cnt)

# print(max_v)






#Greedy 탐색법으로 수행해야 함 -> 최선의 방법 탐색
#회의 종료 시각을 기준으로 오름차순 정렬 후 시작시간과 비교
time_lst.sort(key=lambda x: (x[1], x[0])) #-> 1번 index 기준 오름차순 정렬 후 동일 값은 0번 index 기준 오름차순 정렬

max_v = 0
cur_time = 0


for start_time, end_time in time_lst:
    if start_time >= cur_time:
        max_v += 1
        cur_time = end_time

print(max_v)