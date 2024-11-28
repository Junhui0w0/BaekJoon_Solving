from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip()) #한 변의 길이
lst = []
dp_lst = []

for i in range(n):
    input_lst = list(map(int, input().rstrip().split()))
    dp_lst.append([0]*len(input_lst))
    lst.append(input_lst)

#print(dp_lst) #디버깅
if n == 1:
    print(lst[0][0])

else:
    dp_lst[0][0] = lst[0][0]
    dp_lst[1][0] = lst[0][0] + lst[1][0]
    dp_lst[1][1] = lst[0][0] + lst[1][1]

    for i in range(2, n):
        for j in range(i):
            for v in range(i+1):
                if j - v == -1 or j - v == 0: #오른쪽 대각선, 왼쪽 대각선 아니면 넘김
                    #print(f"i = {i} // j = {j} // v = {v}") #디버깅
                    if dp_lst[i][v] < dp_lst[i-1][j] + lst[i][v]:
                        dp_lst[i][v] = dp_lst[i-1][j] + lst[i][v]

    print(max(dp_lst[n-1]))