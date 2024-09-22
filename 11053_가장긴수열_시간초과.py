from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

length = int(input()) #데이터 길이
data_lst = list(map(int, input().rstrip().split())) #데이터 list
max_length = 0 #데이터의 최대 길이는 1000임 -> 즉, 가장 긴 수열의 길이는 1000

def func(num):
    global max_length
    for v in range(num+1, length):
        if lst[-1] < data_lst[v]:
            lst.append(data_lst[v])
            print('시행: ',lst) #디버깅
            num += 1
            func(num)
        if v == length-1:
            max_length = max(max_length, len(lst))
            lst.pop()

lst = deque()
for i in range(0, length-2):
    if len(lst) == 0:
        lst.append(data_lst[i])
    
    func(i)

print(max_length)

#가장 긴 수열을 찾는 LIS 알고리즘을 사용해야 함