from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

node = int(input()) #노드 갯수
start, end = map(int, input().rstrip().split()) #start는 end의 몇 촌?

time = int(input()) #라인 입력받을 횟수
line_lst = []
Visited = [False] * time #방문했는지?

for i in range(time):
    input_data = list(map(int, input().rstrip().split()))
    line_lst.append(input_data)

#print(line_lst) #디버깅
def DFS(point):
    global cnt
    if point == end:
        return cnt

    for i in range(time):
        if point in line_lst[i]:
            next = sum(line_lst[i]) - point
            if not Visited[i]:
                Visited[i] = True
                cnt += 1 #해당 노드로 이동 했으니 cnt++

                res = DFS(next) #다음 점으로 이동한 결과
                
                if res != -1: #DFS(next)가 -1이 아님, 즉 이동됐을 때, res(결과) return.
                    return res
                cnt -= 1 #만약 다음 점으로 이동했을 떄, 
                         #아무런 조건에 만족하지 않아 -1을 반환 -> 해당 길이 아니므로 이동 횟수를 마이너스 해야함

    return -1 #위 조건을 아무것도 만족하지 않는 경우, DFS(point) 결과는 -1을 반환

cnt = 0
print(DFS(start))
