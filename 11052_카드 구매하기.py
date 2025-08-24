import sys
input = sys.stdin.readline

#입력
    #1. N: 구매하려는 카드 갯수
    #2. [...(N개)]: i번째 카드팩의 금액 & i=카드의 갯수

#실행 및 출력
    #1. N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최대 값을 출력한다.

N = int(input())
card_lst = list(map(int, input().rstrip().split()))
dp_lst = [0] * (N+1) #0~N / index=카드 갯수

for i in range(1, N+1):
    dp_lst[i] = card_lst[0] * i

for card_idx in range(2, N+1): #2~N
    n = 1

    #1. i번째 카드팩 * n 을 통해 최대값 산출
    for loop_idx in range(card_idx, N+1, card_idx):
        dp_lst[loop_idx] = max(dp_lst[loop_idx], card_lst[card_idx-1] * n)
        n += 1

    #2. 이전 카드팩 + i번째 카드팩 갯수를 통한 최대값 산출
        #2-1. 카드팩 1장은 수정불가
        #2-2. i번째 카드팩은 N-i ~ 1번째 카드팩 사용
        #2-3. 마지막 카드팩은 직전 카드팩의 N번 카드팩과의 비교?
    card_max_range = N - card_idx #card_max_range ~ 1번만 사용
    for i in range(1, card_max_range+1):
        dp_lst[i+card_idx] = max(dp_lst[i+card_idx], dp_lst[i] + card_lst[card_idx-1])

print(dp_lst[-1])