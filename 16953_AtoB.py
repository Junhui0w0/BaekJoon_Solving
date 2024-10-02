from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

A,B=map(int, input().rstrip().split()) #A -> B로 바꾸는데 얼마나 많은 연산 필요?

#1. A에 2를 곱한다.
#2. A의 오른쪽에 1을 추가한다.

#A를 시작기점으로 연산1, 연산2 수행
#연산 수행 결과를 계속해서 반복한 결과가 B이면 return cnt,
#만약, 연산 결과가 B를 넘어선다면 return -1

cnt = 0

def DFS(data):
    global cnt
    cnt += 1
    if data == B:
        return cnt
    
    if data > B:
        return -1
    
    gop_data = DFS(2*data)
    if gop_data != -1:
        return cnt #직전 노드로 이동
    cnt -= 1

    add1_data = DFS(10*data + 1)
    if add1_data != -1:
        return cnt
    cnt -= 1

    return -1
    

print(DFS(A))