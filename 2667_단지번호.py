import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

num = int(input().rstrip()) #한 변의 길이(정사각형)
lst = list()
for i in range(num):
    input_data = list(input().rstrip())
    lst.append(input_data)

# print(lst) #디버깅

count = 0
count_lst = [] #단지 당 집의 갯수
#DFS -> stak / LIFO 구조
def DFS(start, end):
    global count
    if start <= -1 or start >= num or end <= -1 or end >= num: #범위를 넘어가는 경우
        return False
    
    if lst[start][end] == '0': #해당 지점이 집이 아닌 경우
        return False
    
    if lst[start][end] == '1': #해당 지점이 집인 경우
        lst[start][end] = '0' #해당 지점에 방문했음을 표시함
        count += 1
        DFS(start + 1, end)
        DFS(start - 1, end)
        DFS(start, end+1)
        DFS(start, end-1)
        return True
    
    return False
    
for i in range(num):
    for j in range(num):
        if DFS(i, j) == True:
            count_lst.append(count)
        count = 0

count_lst.sort()
print(len(count_lst), *count_lst)