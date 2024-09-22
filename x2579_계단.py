from sys import stdin
from collections import deque
N = int(stdin.readline())
stair = [int(stdin.readline()) for _ in range(N)]

count = 0 #연속된 계단을 오른 횟수
total = 0
while(True):
    if(count != 3):
        