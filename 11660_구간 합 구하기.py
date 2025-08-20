#11660_구간 합 구하기.py
import sys
input = sys.stdin.readline

#입력
    #1. N, M -> N: 가로, 세로 크기 / M: 연산 횟수
    #2. [...(N개)] (N줄): 각 칸에 해당하는 값
    #3. [x1, y1, x2, y2] (M줄): 연산에 사용될 범위 (x1,y1 ~ x2,y2 )

#실행 및 출력
    #1. 총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.



#============================================================ 시간초과
# N, M = map(int, input().rstrip().split())

# data_lst = []
# for _ in range(N):
#     input_data = list(map(int, input().rstrip().split()))
#     data_lst.append(input_data)

# pos_lst = []
# for _ in range(M):
#     input_data = list(map(int, input().rstrip().split()))
#     pos_lst.append(input_data) #위치 값은 +1 씩 더 큼

# def get_point(pos_data):
#     x1, y1, x2, y2 = pos_data
#     x1 -= 1
#     y1 -= 1

#     total = 0
#     for x in range(x1, x2):
#         for y in range(y1, y2):
#             total += data_lst[x][y]

#     return total

# for pos in pos_lst:
#     ret = get_point(pos)
#     print(ret)


#============================================================== DP 풀이
#- 각 행에 대해서 값을 증가해서 저장 -> dp[x][0] = lst[x][0] // dp[x][1] = dp[x][0] + lst[x][1] // dp[x][2] = dp[x][1] + lst[x][2]...

N, M = map(int, input().rstrip().split())

data_lst = []
dp = [([0]*N) for i in range(N)]
for i in range(N):
    input_data = list(map(int, input().rstrip().split()))
    data_lst.append(input_data)

    for j in range(N):
        if j == 0:
            dp[i][0] = input_data[0]

        else: #j가 0이 아닌 경우 (1 이상)
            dp[i][j] = dp[i][j-1] + input_data[j] # 이러면 data_lst가 필요한가 ?

pos_lst = []
for _ in range(M):
    input_data = list(map(int, input().rstrip().split()))
    pos_lst.append(input_data)

def get_point(pos_data):
    x1, y1, x2, y2 = pos_data
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    #x -> i에 해당 / y -> j에 해당

    total = 0
    for i in range(x1, x2+1):
        # print(f'dp[{i}][{y2}] // dp[{i}][{y1}]')
        total = total + (dp[i][y2] - dp[i][y1]) + data_lst[i][y1]

    return total

for pos_data in pos_lst:
    ret = get_point(pos_data)
    print(ret)