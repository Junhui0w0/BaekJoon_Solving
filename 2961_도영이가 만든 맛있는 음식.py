import sys
input = sys.stdin.readline

#입력
    #1. N: 재료의 갯수
    #2. [S, B] (N줄) -> S: 신맛의 수치 / B: 쓴맛의 수치

#실행
    #1. 신맛은 곱으로 계산하고, 쓴맛은 합으로 계산한다.
    #2. 재료는 하나 이상을 사용해야 한다. (즉, 재료는 1개 ~ N개 사용 가능)

#출력
    #1. 신맛과 쓴맛의 차이가 가장 작은 요리의 차이를 구한다.

N = int(input())
min_v = float('INF') #양의 무한대 값

food_lst = []
for _ in range(N):
    input_data = list(map(int, input().rstrip().split()))
    food_lst.append(input_data)

tmp = []
def DFS(cur_idx, length):
    global min_v

    if len(tmp) == length:
        s_total = 1
        b_total = 0

        for sour, bitter in tmp:
            s_total = s_total * sour
            b_total = b_total + bitter

        res = abs(s_total - b_total)
        min_v = min(min_v, res)

        if min_v == 0:
            return 'End'

        return True
    
    for idx in range(cur_idx, N):
        tmp.append((food_lst[idx][0], food_lst[idx][1]))
        ret = DFS(idx+1, length)

        if ret == 'End': #결과가 0 == 더 작아질 수 없음
            return 'End'
        
        tmp.pop(-1)


for i in range(1, N+1):
    ret = DFS(0, i)

    if ret == 'End':
        break

print(min_v)