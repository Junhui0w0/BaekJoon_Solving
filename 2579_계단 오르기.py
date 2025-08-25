import sys
input = sys.stdin.readline

#입력
    #1. N: 계단의 수
    #2. [...] (N줄): 각 계단의 가중치 값

#실행
    #1. 계단은 한 번에 한 계단 또는 두 계단 씩 오를 수 있다.
    #2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. (단, 시작점은 계단에 포함되지 않는다.)
    #3. 마지막 도착 계단은 반드시 밟아야 한다. (즉, 마지막 계단의 move != 0 이어야 함)

#출력
    #1. 해당 게임에서 얻을 수 있는 총 점수의 최대값을 출력한다.

N = int(input())

stair_lst = []
for _ in range(N):
    input_data = int(input().rstrip())
    stair_lst.append(input_data)

dp_lst = [([0]*3) for _ in range(N)]
dp_lst[0][0] = 0
dp_lst[0][1] = stair_lst[0]

for idx in range(1, N):
    #1. 다음 dp_lst[idx][0]에는 직전(dp_lst[idx-1][0], dp_lst[idx-1][1], dp_lst[idx-1][2])이 다 올 수 있음
        #이때, 다음 계단으로 넘어가기 위해서는 반드시 하나의 계단 또는 두개의 계단을 가야하므로 지속해서 안밟을 수는 없음 -> dp_lst[idx-1][0] 삭제
    dp_lst[idx][0] = max(dp_lst[idx-1][1], dp_lst[idx-1][2])

    #2. 다음 dp_lst[idx][1]에는 dp_lst[idx-1][0]의 값만 올 수 있음
    dp_lst[idx][1] = dp_lst[idx-1][0] + stair_lst[idx]

    #3. 다음 dp_lst[idx][2]에는 dp_lst[idx-1][1]의 값만 올 수 있음
    dp_lst[idx][2] = dp_lst[idx-1][1] + stair_lst[idx]

max_v = max(dp_lst[-1][1:])
print(max_v)