#가장 긴 수열 - LIS (Longest Increasing Sequence)
#DP의 한 예시, 시계열 데이터 분석에 주로 사용

from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

length = int(input())
data_lst = list(map(int, input().rstrip().split())) #데이터 저장 list

def lis(lst):
    lis_lst = [1] * length #DP list
    
    for i in range(1, length):
        for j in range(0, i):
            if lst[i] > lst[j] and lis_lst[i] < lis_lst[j] + 1:
                lis_lst[i] = lis_lst[j] + 1

    max_len = 0
    
    for i in lis_lst:
        max_len = max(max_len, i)

    return max_len

print(lis(data_lst))