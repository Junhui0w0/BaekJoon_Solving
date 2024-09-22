import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

length = int(input()) #데이터 갯수
data_lst = [0] * length #데이터를 입력받아 저장할 list
is_go = [1] *(length+1) #N번이 이미 나왔는지 검사할 list

for i in range(length):
    data = int(input())
    data_lst[i] = data


ans = ('+\n' * data_lst[0]) + '-\n'
is_go[data_lst[0]] = 0 #갔음을 표시
pop_data = data_lst[0] #pop한 데이터

for i in range(1, length):
    if pop_data > data_lst[i]:
        is_go[data_lst[i]] = 0
        total = sum(is_go[data_lst[i]:pop_data+1])
        
        if total != 0: #is_go 범위에 1이 있다는 증거 -> 해당 지점을 pop하지 않은 것
            ans = 'NO'
            break
        
        ans += '-\n'
        pop_data = max(data_lst[i], pop_data)

    elif pop_data < data_lst[i]:
        is_go[data_lst[i]] = 0
        plus_msg = (data_lst[i] - pop_data) * '+\n' + '-\n'
        ans += plus_msg

        pop_data = max(data_lst[i], pop_data)

print(ans)