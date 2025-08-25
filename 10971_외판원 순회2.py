import sys
input = sys.stdin.readline

#입력
    #1. N: 도시의 수
    #2. [...(N개)] (N줄) -> lst[x][y] -> x: 출발도시 / y: 도착도시 / value=비용

#실행
    #1. 도로 사이에 도로가 존재하지 않을 수 있다.
    #2. i번 도시에서 j번 도시에 도착하는 비용과 j번 도시에서 i번 도시에 도착하는 비용이 서로 다를 수 있다. (즉, 동일하거나 다르다.)
    #3. 출발도시는 임의로 정하며, 순회 경로의 마지막은 출발도시여야 한다. 
        #ex) 출발도시=1번 이다 == 1 -> 2 -> 3 -> 1
        #ex) 즉, [1->2 비용 + 2->3 비용 + 3->1 비용] 만큼의 비용이 필요하다.

#출력
    #1. 외판원 순회에 필요한 최소 비용을 출력한다.

N = int(input())

w = []
for _ in range(N):
    input_data = list(map(int, input().rstrip().split()))
    w.append(input_data)

min_v = float('INF')

def DFS(start_city, cur_city, total, city_length):
    global min_v

    if city_length == N: #모든 도시 순회한 경우
        if w[tmp[-1]][start_city] == 0:
            return False

        total = total + w[tmp[-1]][start_city]
        # print(total)
        min_v = min(total, min_v)
        return True
    
    for i in range(N):
        if visited[i] == False: #i번째 도시에 가지 않았다면?
            if w[cur_city][i] == 0: #cur_city -> i 도시로 가는 도로가 없다면? 해당 순회는 틀려먹음
                return True
            
            visited[i] = True
            tmp.append(i)
            DFS(start_city, i, total + w[cur_city][i], city_length+1)
            tmp.pop(-1)
            visited[i] = False
            
        

for i in range(N):
    tmp = []
    tmp.append(i)

    visited = [False] * N
    visited[i] = True #해당 도시 방문 (시작점이기 때문)

    DFS(i,i,0, 1)

print(min_v)