from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

#입력
    #1. n,m -> n: {0}부터 {n}까지의 집합 (N+1개) / m: 연산 갯수
    #2. [oper, a, b] -> oper: 연산의 종류 / a & b: 연산에 사용되는 집합 번호

#실행
    #1. 연산의 종류는 0과 1로 구분된다.
        #1-1. 0은 두 집합을 합집합 연산하는 것 이다.
        #1-2. 1은 두 집합이 서로 같은 집합인지 판별하는 것 이다.

#출력
    #1. 연산이 1 일 때, 두 집합이 서로 같은 집합에 있으면 YES를, 그렇지 않으면 0을 출력한다.

n,m = map(int, input().rstrip().split())
parent_lst = [i for i in range(n+1)] #index = 0~n

# def find_parent(lst, idx):
#     cur_parent = lst[idx]

#     if cur_parent != idx:
#         cur_parent = find_parent(lst, cur_parent)

#     return cur_parent 

def find_parent(lst, idx):
    if lst[idx] != idx:
        lst[idx] = find_parent(lst, lst[idx])

    return lst[idx]

#두 find_parent의 차이점은 아래와 같다.
    #- 첫번째 find_parent는 별도의 변수(cur_parent)를 선언하여 가시성을 높였지만, 실제 lst[idx]의 값을 변경하지 못한다.
    #- 따라서 '경로압축' 이 정상적으로 작동되지 않아 시간복잡도가 O(NlogN)이 아닌, O(N)이 발생한다.


def union(lst, indexA, indexB):
    rootA = find_parent(lst, indexA)
    rootB = find_parent(lst, indexB)

    if lst[rootA] < rootB:
        lst[rootB] = rootA

    else:
        lst[rootA] = rootB

    return

for i in range(m):
    oper, start, end = map(int, input().rstrip().split())

    if oper == 0: #union
        union(parent_lst, start, end)

    else: #동일 집합?
        start_parent = find_parent(parent_lst, start)
        end_parent = find_parent(parent_lst, end)

        if start_parent == end_parent: #동일 부모 == 동일 집합?
            print('YES')

        else:
            print('NO')