from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input()) #한 변의 길이 (정사각형)
lst = []

for i in range(N):
    input_data = list(map(str, input().rstrip()))
    lst.append(input_data)

move_lst = [(-1,0), (1,0), (0,1), (0,-1)]

def BFS(x,y,alphabet):
    if alphabet == 'G':
        alphabet1 = 'R'
        lst[x][y] = alphabet1+alphabet1 #RR / GG / BB

    else:
        lst[x][y] = alphabet+alphabet
    
    for dx, dy in move_lst:
        if x + dx <= -1 or x + dx >= N or y + dy <= -1 or y + dy >= N:
            continue

        if lst[x+dx][y+dy] == alphabet:
            BFS(x+dx, y+dy, alphabet)

    return True

total1 = 0
total2 = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 'R' or lst[i][j] == 'G' or lst[i][j] == 'B':
            total1 += 1

            if lst[i][j] == 'B':
                total2 += 1

            BFS(i,j,lst[i][j])

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'RR':
            total2 += 1
            BFS(i,j,'RR')

print(total1, total2)