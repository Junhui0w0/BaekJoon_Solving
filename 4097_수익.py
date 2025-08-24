import sys
input = sys.stdin.readline

#입력
    #1. N: 테스트 케이스 갯수
    #2. [profit] (N줄): 각 일수별 수익

#실행
    #1. N이 0이 될 경우 종료된다.

#출력
    #1. 가장 많은 수익을 올린 구간의 수익을 출력한다. (단, 구간이 비어 있으면 안 된다)

while(True):
    N = int(input())

    if N == 0:
        break

    profit_lst = []
    for _ in range(N):
        input_data = int(input().rstrip())
        profit_lst.append(input_data)

    MIN_V = float('INF') * -1
    max_v = float('INF') * -1

    dp_lst = [MIN_V] * (N)
    dp_lst[0] = profit_lst[0] #초기화

    if N == 1:
        print(dp_lst[0])
        continue

    for i in range(1, N):
        dp_lst[i] = max(profit_lst[i], dp_lst[i-1] + profit_lst[i])
        max_v = max(max_v, dp_lst[i])

    print(max_v)