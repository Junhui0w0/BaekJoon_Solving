# -> 마시지 않는 경우의 수도 고려해야 함

# from collections import deque
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n = int(input().rstrip()) #마실 포도잔의 수
# lst = [] #각 포도잔의 양
# for i in range(n):
#     mL = int(input().rstrip())
#     lst.append(mL)

# dp_lst = [[] for i in range(n)]
# dp_lst[0] = [lst[0], 1, 0, 0]

# #print(dp_lst) #디버깅

# for i in range(1, n):
#     first_total = dp_lst[i-1][0]
#     first_count = dp_lst[i-1][1]

#     second_total = dp_lst[i-1][2]
#     second_count = dp_lst[i-1][3]

#     if first_count < 2:
#         first_total += lst[i]
#         first_count += 1
#     else:
#         first_count = 0

#     if second_count < 2:
#         second_total += lst[i]
#         second_count += 1
#     else:
#         second_count = 0

#     dp_lst[i] = [first_total, first_count, second_total, second_count]

# print(dp_lst) #디버깅
# print(max(dp_lst[n-1]))