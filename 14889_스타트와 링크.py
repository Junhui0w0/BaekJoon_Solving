import sys
input = sys.stdin.readline

#입력
    #1. N: 사람 수
    #2. [...(N개)] (N줄): i행 j열에 해당하는 능력치

#실행
    #1. 각 팀(스타트팀 & 링크팀)의 능력치는 아래와 같이 계산할 수 있다.
        #1-1. i번 사람과 j번 사람이 같은 팀일 경우 능력치의 합은 lst[i][j] + lst[j][i] 이다.
        #1-1. lst[i][i] = 0 이다. (즉, 자기자신은 제외한다.)
    #2. N은 항상 짝수이다.

#출력
    #1. 각 팀의 능력치합이 최소가 되도록 출력한다.

N = int(input())

person_per_team = N//2 #한 팀에 들어갈 수 있는 팀

ability_lst = []
for _ in range(N):
    input_data =list(map(int, input().rstrip().split()))
    ability_lst.append(input_data)

team_lst = []

def calc_ability(team):
    point = 0

    for x in team:
        for y in team:
            point += ability_lst[x][y]

    return point

def DFS(cur_idx):
    global min_v

    if len(tmp) == person_per_team:
        lst = [i for i in range(N)] #0~N-1번 팀원

        for i in tmp[-1:-1*person_per_team-1:-1]:
            lst.pop(i)

        # print(f'start: {tmp} // link: {lst}')
        start_team_point = calc_ability(tmp)
        link_team_point = calc_ability(lst)
        min_v = min(min_v, abs(start_team_point - link_team_point))

        return True
    
    for i in range(cur_idx, N):
        tmp.append(i)
        DFS(i+1)
        tmp.pop(-1)

min_v = float('INF')
tmp = [0]
DFS(1)
print(min_v)