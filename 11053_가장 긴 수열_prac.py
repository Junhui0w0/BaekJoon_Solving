import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

length = int(input()) #데이터 갯수 입력
data_lst = list(map(int, input().rstrip().split())) #데이터 입력
dp_lst = [1] * length

for i in range(1, length):
    for j in range(0, i):
        if data_lst[i] > data_lst[j] and dp_lst[i] < dp_lst[j] + 1:
            dp_lst[i] = dp_lst[j] + 1

max_len = 0
for i in dp_lst:
    max_len = max(max_len, i)

print(max_len)