from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
# visited = [False] * ((K-1)*2)
visited = [False] * 200000
q= deque() 
q.append((N,0))

while(q):
    current_pos, count = q.popleft()

    if current_pos < 0 or current_pos > 100000:
        continue
    
    if current_pos == K:
        print(count)
        # print("탐색완료") #디버깅
        break

    if visited[current_pos] == True:
        continue

    visited[current_pos] = True
    count += 1

    if current_pos > K:
        q.append((current_pos - 1, count))

    elif current_pos < K:
        q.append((current_pos - 1, count))
        q.append((current_pos * 2, count))
        q.append((current_pos + 1, count))