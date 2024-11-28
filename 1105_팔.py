from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

L, R = map(int, input().rstrip().split())
L_lst = list(map(int, str(L)))
R_lst = list(map(int, str(R)))

cnt = 0
lst = []
if len(L_lst) != len(R_lst):
    print(0)

else:
    for i in range(len(L_lst)):
        if L_lst[i] != R_lst[i]:
            break

        lst.append(L_lst[i])

    for i in lst:
        if i == 8:
            cnt += 1

    print(cnt)