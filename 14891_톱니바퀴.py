import sys
import copy
from collections import deque
input = sys.stdin.readline

#입력
    #1. [...] (4줄): N번 줄 = N번 톱니바퀴의 상태
    #2. k: 회전 횟수
    #3. [number, direction] -> number: 회전시킬 톱니바퀴 번호 / direction: 회전시킬 방향 (1=시계방향 / -1=반시계방향)

#실행
    #1. 톱니바퀴의 상태는 0 또는 1로 구성되어 있으며 0은 N극을, 1은 S극을 나타낸다.
    #2. 특정 톱니바퀴를 회전할 때, 맞닿아 있는 부분의 극이 같으면 회전하지 않고, 극이 다르면 돌아간 톱니바퀴의 반대 방향으로 돈다.

#출력
    #1. k번 회전 시킨 이후 4개의 톱니바퀴 점수의 합을 출력한다. 이때 점수는 아래와 같이 계산한다.
        #1-1. 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
        #1-2. 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
        #1-3. 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
        #1-4. 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

topni_lst = [None]
for _ in range(4):
    input_data = deque(map(int, input().rstrip()))
    topni_lst.append(input_data)

k = int(input())

rotate_lst = []
for _ in range(k):
    input_data = list(map(int, input().rstrip().split()))
    rotate_lst.append(input_data) #[0]=회전시킬 톱니번호 / [1]=방향 -> -1=반시계 / 1=시계

#- 톱니바퀴 비교 번호는 아래와 같음
    #- topni_lst[1][2] vs topni_lst[2][6] -> 같다? 현재 회전 방향의 반대로 회전
    #- topni_lst[2][2] vs topni_lst[3][6]
    #- topni_lst[3][2] vs topni_lst[4][6]





# #========================================================================== 문제 이해 잘못함
# def rotate(topni_number, cur_direction):
#     is_rotate[topni_number] = True #topni_number 번째 톱니는 회전했다.

#     #1. 톱니 회전
#     # tmp = topni_lst[topni_number].copy()
#     tmp = copy.deepcopy(topni_lst[topni_number])

#     if cur_direction == -1: #반시계 방향 -> [0] pop 후 append
#         pop_data = tmp.popleft()
#         tmp.append(pop_data)

#     elif cur_direction == 1: #시계 방향 -> [-1] pop 후 appendleft -> deque가 편할듯
#         pop_data = tmp.pop()
#         tmp.appendleft(pop_data)

#     topni_lst[topni_number] = tmp #회전한 톱니 적용
#     #2. 톱니를 회전함으로써 양 옆에 있는 톱니도 회전하는가?
#         #- 이는 비교했을 때 서로 다른 극이면 됨
#     if topni_number == 1: #이 전에 회전한 톱니가 1번일 때 -> 2번 톱니랑만 비교하면 됨
#         if topni_lst[1][2] != topni_lst[2][6] and is_rotate[2] == False: #서로 다른극 and 2번 톱니가 회전 하지 않았으면 회전해야겠지?
#             rotate(2, cur_direction*-1)

#     elif topni_number == 2: #이 전에 회전한 톱니가 2번일 때 -> 1 & 3번 톱니 비교
#         if topni_lst[1][2] != topni_lst[2][6] and is_rotate[1] == False: #서로 다른 극 and 1번 톱니가 아직 회전X -> 회전시켜
#             rotate(1, cur_direction*-1)

#         if topni_lst[2][2] != topni_lst[3][6] and is_rotate[3] == False:
#             rotate(3, cur_direction*-1)

#     elif topni_number == 3:
#         if topni_lst[2][2] != topni_lst[3][6] and is_rotate[2] == False:
#             rotate(2, cur_direction*-1)

#         if topni_lst[3][2] != topni_lst[4][6] and is_rotate[4] == False:
#             rotate(4, cur_direction*-1)

#     else: #톱니가 4번인 경우
#         if topni_lst[3][2] != topni_lst[4][6] and is_rotate[3] == False:
#             rotate(3, cur_direction*-1)
    
#     return True

# for cur_topni, direciton in rotate_lst:
#     is_rotate = [False, False, False, False, False]
#     rotate(cur_topni, direciton)

# total = 0
# for idx in range(1, 5): #1~4
#     if topni_lst[idx][0] == 1: #12시 방향이 S극(1)
#         total += 2**(idx-1)

# print(total)
# #===========================================================================
# #모든 상황을 확인한 후에 한번에 회전시켜야 함.

def check(topni_num, cur_direction): #회전시킬 톱니 번호 반환하는 함수
    if topni_num == 1: #1번 톱니 회전한다? -> 2번 톱니랑만 비교
        if is_rotate[2] == 'not rotate' and topni_lst[1][2] != topni_lst[2][6]: #회전 X and 서로 다른 극 -> 회전
            is_rotate[2] = cur_direction * -1
            check(2, cur_direction * -1)

    elif topni_num == 2: #2번 톱니 회전 -> 1번 & 3번 비교
        if is_rotate[1] == 'not rotate' and topni_lst[1][2] != topni_lst[2][6]:
            is_rotate[1]=cur_direction * -1
            check(1, cur_direction * -1)

        if is_rotate[3] == 'not rotate' and topni_lst[2][2] != topni_lst[3][6]:
            is_rotate[3] = cur_direction * -1
            check(3, cur_direction * -1)

    elif topni_num == 3:
        if is_rotate[2] == 'not rotate' and topni_lst[2][2] != topni_lst[3][6]: #2번
            is_rotate[2]=cur_direction * -1
            check(2, cur_direction * -1)

        if is_rotate[4] == 'not rotate' and topni_lst[3][2] != topni_lst[4][6]: #4번
            is_rotate[4] = cur_direction * -1
            check(4, cur_direction * -1)

    else: #4번 톱니 회전 -> 3번
        if is_rotate[3] == 'not rotate' and topni_lst[3][2] != topni_lst[4][6]: #회전 X and 서로 다른 극 -> 회전
            is_rotate[3] = cur_direction * -1
            check(3, cur_direction * -1)
    
    return True

def rotate(topni_num, direciton):
    tmp = copy.deepcopy(topni_lst[topni_num])

    if direciton == -1: #반시계
        pop_data = tmp.popleft()
        tmp.append(pop_data)

    elif direciton == 1: #시계
        pop_data = tmp.pop()
        tmp.appendleft(pop_data)

    topni_lst[topni_num] = tmp
    return True

for cur_topni, cur_direciton in rotate_lst:
    is_rotate = ['not rotate', 'not rotate', 'not rotate', 'not rotate', 'not rotate']
    is_rotate[cur_topni] = cur_direciton
    check(cur_topni, cur_direciton) #회전할 톱니들이 전부 기록

    for idx in range(1, 5): #idx=톱니 번호
        if is_rotate[idx] == 'not rotate':
            continue
        
        rotate(idx, is_rotate[idx])

total = 0
for idx in range(1, 5): #1~4
    if topni_lst[idx][0] == 1: #12시 방향이 S극(1)
        total += 2**(idx-1)

print(total)