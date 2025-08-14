# dict1 = dict()

# while(True):
#     a = int(input())

#     if a == 0 :
#         break

#     if a in dict1:
#         dict1[a] = dict1[a] + 1

#     else:
#         dict1[a] = 1

# print(dict1)

import sys
input = sys.stdin.readline

#입력
    #1. N: 입력할 카드 갯수
    #2. [...] (N개): 숫자 카드에 적힌 값
    #3. M: 플레이어가 가지고 있는 가를 탐색할 카드 갯수
    #4. [...] (M개): 카드 값

#실행 및 출력
    #1. 전체 숫자 카드 정보에 기반하여 플레이어가 갖고 있는 카드의 갯수가 총 몇개 있는지 출력한다.

N = int(input())
stored_lst = list(map(int, input().rstrip().split()))

dict1 = dict()
for card_num in stored_lst:
    if card_num in dict1:
        dict1[card_num] += 1

    else:
        dict1[card_num] = 1

M = int(input())
player_lst = list(map(int, input().rstrip().split()))

for ans_num in player_lst:
    if ans_num not in dict1:
        print(0, end=' ')

    else:
        print(dict1[ans_num], end=' ')