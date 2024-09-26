#https://www.acmicpc.net/board/view/134999 <- 참고해서 풀어보셈 ㅈㄴ 간결하네
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

Node = int(input().rstrip()) #노드 갯수
line_lst = [0] * (Node-1) #간선 정보 List

q = deque() #최상위 부모 1이 포함된 간선

for i in range(Node-1):
    data = list(map(int, input().rstrip().split())) #입력한 간선
    line_lst[i] = data
    
    if 1 in data:
        q.append(data)

# print("line_lst -> ", line_lst) #디버깅
# print('q -> ',q)

output_lst = [False] * (Node+1)
output_lst[0] = 1 #0의 부모노드는 없음
output_lst[1] = 1 #1은 최상위 부모임

def BFS(start, end):
    for line in line_lst:
        if output_lst[line[0]] != False and output_lst[line[1]] != False:  #두 노드 모두 부모가 정해진 경우 -> vistied된 경우
            continue
        
        else:
            if start in line or end in line:
                if output_lst[start] == False: #부모 노드가 정해져 있지 않은 경우
                    output_lst[start] = end

                elif output_lst[end] == False:
                    output_lst[end] = start

                BFS(line[0], line[1])

while(q): #q가 빌 때 까지 반복
    start, end = q.popleft() #선입선출 FIFO -> BFS
    BFS(start, end)

output_lst.pop(0)
output_lst.pop(0)
print(*output_lst)