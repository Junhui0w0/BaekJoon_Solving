from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split()) #0~n의 원소 / 총 m개의 연산
lst = [[i] for i in range(n+1)]
# print(lst) #디버깅

def find_min(lst, min_v):
    if min_v == min(lst[min_v]):
        return min_v
    
    else:
        tmp = find_min(lst, min(lst[min_v]))
        if tmp != False:
            return tmp

    return False

for i in range(m):
    command = list(map(int, input().rstrip().split())) #집합연산 / a집합 / b집합

    if command[0] == 0: #합집합 수행
        # lst[command[1]].append(command[2]) #a집합에 b원소 삽입
        lst[find_min(lst, min(lst[command[1]]))].append(command[2])

        # lst[command[2]].append(command[1]) #b집합에 a원소 삽입
        lst[find_min(lst, min(lst[command[2]]))].append(command[1])

    elif command[0] == 1: #원소 포함 여부 확인
        if command[2] in lst[find_min(lst, min(lst[command[1]]))] or command[1] in lst[find_min(lst, min(lst[command[2]]))]:
            print('yes')
        else:
            print('no')

