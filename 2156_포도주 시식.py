from collections import deque
import sys
input =sys.stdin.readline

#입력
    #1. n: 포도주 잔의 갯수
    #2. [...] (n줄): 각 포도잔에 채워진 포도주스의 양

#실행
    #1. 포도주 잔을 선택하면, 해당 잔에 들어있는 모든 주수를 다 마셔야 한다.
    #2. 연속으로 놓여 있는 3잔을 모두 마실 수 없다. (1->2->3 불가, 1->2->4 가능)

#출력
    #1. 최대로 마실 수 있는 포두주의 양을 출력한다.

n = int(input())

podo_lst = []
for _ in range(n):
    input_data = int(input().rstrip())
    podo_lst.append(input_data)


if n >= 2:
    dp_lst = [([-1] * 3) for _ in range(n)]
    dp_lst[0] = podo_lst[0]
    # dp_lst[1] = [podo_lst[1], (podo_lst[0][0], 0), (podo_lst[0][0] + podo_lst[1][0], 2)]
    # dp_lst[1] = [podo_lst[0][0], podo_lst[1][0], podo_lst[0][0] + podo_lst[1][0]]
    dp_lst[1][0] = podo_lst[0]
    dp_lst[1][1] = podo_lst[1]
    dp_lst[1][2] = podo_lst[0] + podo_lst[1]

    for i in range(2, n): 
        for j in range(3): #j = move / dp_lst[i] = podo
            if j == 0: #직전의 0은 다음 dp의 1로 감
                dp_lst[i][1] = dp_lst[i-1][0] + podo_lst[i]
                dp_lst[i][0] = max(dp_lst[i][0], dp_lst[i-1][0]) #다음 잔을 마시지 않는 경우는 직전에 몇잔을 마셨는가에 상관없이 넘기기가 가능함

            elif j == 1: #직전의 1은 다음 dp의 0 또는 2로 감
                dp_lst[i][0] = max(dp_lst[i][0], dp_lst[i-1][1])
                dp_lst[i][2] = dp_lst[i-1][1] + podo_lst[i]

            elif j == 2: #직전의 2는 다음 dp의 0으로 감
                dp_lst[i][0] = max(dp_lst[i][0], dp_lst[i-1][2])
                
    max_v = -1
    for podo in dp_lst[-1]:
        max_v = max(max_v, podo)

    print(max_v)

else:
    print(podo_lst[0])