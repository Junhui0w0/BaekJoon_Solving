import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

length = int(input())
data_lst = [0] * length

for i in range(length):
    data = int(input())
    data_lst[i] = data

ans = ''
idx = 0

plus = 0
minus = 0

def func(pop_data1):
    global ans, idx, minus
    ans += '-\n'
    minus += 1
    pop_data1 = data_lst[idx]
    idx += 1
    
    if idx <= length-1:
        if data_lst[idx] < pop_data1:
            func(pop_data1)

pop_data = 0

for i in range(length):
    data = i+1 #List의 index는 i / 넣을 데이터는 i + 1
    
    if data != data_lst[idx]:
        ans += '+\n'
        plus += 1

    elif data == data_lst[idx]:
        ans += '+\n-\n' #넣고 바로 빼야함
        pop_data = data
        idx += 1
        plus += 1
        minus += 1

    if data_lst[idx] < pop_data:
        func(pop_data)

if plus == minus:
    print(ans)
else:
    print("NO")

#반례 - https://www.acmicpc.net/board/view/143996
