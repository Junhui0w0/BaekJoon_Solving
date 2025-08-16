from collections import deque
import sys
input = sys.stdin.readline

total_len = 0

N = int(input().rstrip()) #1~N까지 자연수
length = len(str(N))
# print(length)

if length == 1:
    print(N)

else:
    total = 0

    for i in range(1, length): #1 ~ N-1
        total += 9 * (i * (10**(i-1)))

    tmp = '1' * (length-1)
    tmp = int(tmp)
    
    total += length * (N- 9*tmp)

    print(total)