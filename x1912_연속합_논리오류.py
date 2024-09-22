from collections import deque
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

length = int(input())
data_lst = list(map(int, input().rstrip().split())) #데이터 저장 리스트
max_lst = []
lst_in_max_data = max(data_lst)

if length >= 4:
    dp_max_data = max(data_lst[0] + data_lst[2] , data_lst[1] + data_lst[2], sum(data_lst[:3]))

    for i in range(3, length):
        dp_max_data = max(dp_max_data + data_lst[i], data_lst[i-1] + data_lst[i], sum(data_lst[:i+1]))
        max_lst.append(dp_max_data)

    print(max(max(max_lst), lst_in_max_data))

elif length == 3:
    dp_max_data = max(data_lst[0] + data_lst[2] , data_lst[1] + data_lst[2], sum(data_lst[:]))
    print(max(dp_max_data, lst_in_max_data))

elif length == 2:
    print(max(lst_in_max_data, sum(data_lst[:])))

elif length == 1:
    print(data_lst[0])