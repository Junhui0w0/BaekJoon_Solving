import sys
import heapq
input = sys.stdin.readline

#입력
    #1. n, k -> n: 동전의 갯수 / k: 주어진 동전으로 만들 금액
    #2. coin (n줄): 각 동전의 금액

#실행
    #1. 주어진 동전은 제한없이 사용할 수 있다. (즉, 같은 동전을 여러개 사용해도 된다.)

#출력
    #1. k를 만들기 위해 필요로 하는 동전의 최소 갯수를 출력한다.

n, k =map(int, input().rstrip().split())

MAX_V = float('INF')
dp_lst = [MAX_V] * (k+1) #index=0~k -> index=금액 이라고 가정할 때, 지정된 값은 해당 금액을 만들기 위해 필요로하는 동전의 갯수를 의미한다.
dp_lst[0] = 0 #0원은 만들 수 없음 -> 동전은 100,000 보다 작거나 같은 자연수

coin_lst = []
heap_lst = [] #- 다익스트라 AL 활용 (cnt, coin) 형태로 삽입
for _ in range(n):
    input_data = int(input().rstrip())

    if input_data > k: #- 주어진 coin이 만들고자하는 금액(k)보다 크다? -> 그건 필요 없는 coin임
        continue

    coin_lst.append(input_data)
    heapq.heappush(heap_lst, (1, input_data))

while(heap_lst):
    cnt, coin_index = heapq.heappop(heap_lst)

    if dp_lst[coin_index] < cnt: #지금까지 지나온 경로(코인의 갯수)보다 기존에 저장된 갯수가 더 적다면? -> 굳이 갈 필요 없음
        continue #같으면 다음 경로에 따라 결과가 달라지기에 등호는 삭제

    dp_lst[coin_index] = cnt

    for coin_data in coin_lst:
        total_cnt = cnt + 1 #다음(next_index)으로 넘어가는데 필요한 코인 수
        next_index = coin_data + coin_index

        if next_index > k:
            continue

        if dp_lst[next_index] <= total_cnt: #지금까지 온 경로보다 이전에 온 경로가 더 효율적이라면 굳이 갈 필요 없음
            continue

        dp_lst[next_index] = total_cnt
        heapq.heappush(heap_lst, (total_cnt, next_index))

if dp_lst[k] == MAX_V:
    print(-1)

else:
    print(dp_lst[-1])