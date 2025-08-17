from collections import deque
import sys
input = sys.stdin.readline

#입력
    #1. N, M -> N: 앞마당 길이 / M: 대회의 시간
    #2. [...] (N개): 각 위치에 따른 눈덩이의 양

#실행
    #1. 눈덩이는 M초 동안 굴릴 수 있다.
    #2. 눈덩이는 아래 두 가지 방식으로만 굴릴 수 있다.
        #2-1. 현재 위치에서 +1칸 굴리면, 눈덩이의 크기는 <본래크기 + 해당 위치에 있는 눈의 양> 이다.
        #2-2. 현재 위치에서 +2칸 굴리면, 눈덩이의 크기는 <본래크기//2 + 해당 위치에 있는 눈의 양> 이다.
    #3. 눈덩이를 굴릴 경우 시간은 1초씩 증가된다.

#출력
    #1. 눈덩이의 최대 크기를 출력한다.
        #1-1. 단, 앞마당 끝에 도달하는 순간 남은 시간에 상관없이 대회는 종료된다.

N, M = map(int, input().rstrip().split())
snow_lst = list(map(int, input().rstrip().split()))
dp_lst = [-1] * N

#==============================================# 93% 터짐
# max_v = -1
# def DFS(cur_idx, cur_second, cur_total):
#     global max_v

#     if cur_second == M or cur_idx == N-1: #시간 종료
#         max_v = max(max_v, cur_total)
#         return True
    
#     for i in range(cur_idx, N):
#         if tmp[-1] + 1 == i: #한칸 가는 경우
#             tmp.append(i)
#             DFS(i+1, cur_second+1, cur_total+snow_lst[i])
#             tmp.pop(-1)

#         elif tmp[-1] + 2 == i: #두칸 가는 경우
#             tmp.append(i)
#             DFS(i+1, cur_second+1, (cur_total // 2) + snow_lst[i])
#             tmp.pop(-1)

#         else:
#             break
            
# if N != 1:
#     tmp = [0] #idx 삽입 / 시작위치(0) -> 한칸 가는 경우
#     DFS(1, 1, 1 + snow_lst[0]) #시작 무게는 항상1

#     tmp = [1] #idx 삽입 / 시작위치(0) -> 두칸 가는 경우
#     DFS(2, 1, snow_lst[1])

#     print(max_v)

# else:
#     print(1 + snow_lst[0])
#==============================================# 93% 터짐


#- N=1 / 2이상 인 경우로 크게 구분 가능
if N >= 2: #기본인 경우
    max_v = -1

    tmp = [(1, 0, -1, False), (1, 0, -1, True)] #- (현 눈덩이 크기, 시간(초), idx) 형태의 tuple로 삽입
        #1. 현 눈덩이 / 현 시간 / 시작 위치 / 1칸 던졌는가? (True=ㅇㅇ)
        #2. 현 눈덩이 / 현 시간 / 시작 위치 / 1칸 던졌는가? (False->2칸 던짐)

    while(tmp):
        cur_snow, cur_second, cur_idx, one_or_two = tmp.pop(0)

        if cur_second == M or cur_idx == N-1:
            max_v = max(max_v, cur_snow)
            continue

        if one_or_two == True: #현 위치에서 한칸 던지겠다 -> cur_idx+1 / cur_second+1 / cur_snow+=snow_lst[cur_idx+1]
            if cur_idx + 1 >= N:
                continue

            cur_idx += 1 #위치 변경
            cur_second += 1 #시간 변경
            cur_snow += snow_lst[cur_idx] #눈의 총 량 변경
            
            tmp.append((cur_snow, cur_second, cur_idx, True))
            tmp.append((cur_snow, cur_second, cur_idx, False))

        else:
            if cur_idx + 2 >= N:
                continue

            cur_idx += 2
            cur_second += 1
            cur_snow = cur_snow // 2 + snow_lst[cur_idx]

            tmp.append((cur_snow, cur_second, cur_idx, True))
            tmp.append((cur_snow, cur_second, cur_idx, False))

    print(max_v)

else:
    print(1 + snow_lst[0])