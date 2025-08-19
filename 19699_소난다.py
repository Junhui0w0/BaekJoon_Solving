import sys
input = sys.stdin.readline

#입력
    #1. N, M -> N:소들의 수 / M: 선별할 소의 수
    #2. [...(N개)]: 각 소들의 무게

#실행
    #1. 전체 N마리의 소들 중 M마리씩 선별한다.
    #2. 이때, 선별한 소들의 무게 합은 소수(prime)이 되어야 한다.

#출력
    #1. M마리 소들의 몸무게 합으로 만들 수 있는 모든 소수를 오름차순으로 출력한다. 만약 그러한 경우가 없다면 -1을 출력한다.

N, M =map(int, input().rstrip().split())
weight_lst = list(map(int, input().rstrip().split()))

weight_lst.sort()
max_weight_pair = sum(weight_lst[-1 * M:])

prime_lst = [True] * (max_weight_pair+1) #0~max_weight_pair 까지의 범위 중 소수 구할 수 있음
prime_lst[0] = False
prime_lst[1] = False
for i in range(2, int(max_weight_pair ** 0.5)+1): #2~ 루트 max_weight_pair 까지
    for j in range(2*i, max_weight_pair+1, i):
        prime_lst[j] = False

answer = []

tmp = []
def DFS(cur_idx):
    if len(tmp) == M:
        total = sum(tmp)

        if total not in answer and prime_lst[total] == True:
            answer.append(total)

        return True
    
    for i in range(cur_idx, N):
        tmp.append(weight_lst[i])
        DFS(i+1)
        tmp.pop(-1)

DFS(0)
if answer:
    answer.sort()
    print(*answer)

else:
    print(-1)