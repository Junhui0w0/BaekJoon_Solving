from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

time = int(input()) #반복횟수

#소수 List
prime_lst = [True] * 10001 #(index가 0~10000인 lst)
prime_lst[0] = False
prime_lst[1] = False #0과 1은 소수X

for i in range(2, int((10000**0.5)+1), 1):
    for j in range(2*i, 10001, i): #j는 i의 배수이기에 소수가 아님
        prime_lst[j] = False

#print(prime_lst) #디버깅


#시간초과 - 반복문이 너무 많고, 탐색할 idx도 너무 넓음
# for i in range(time):
#     data1 = 0
#     data2 = 0
#     min_data = 10001
#     data = int(input()) #data는 4이상 10000이하

#     for j in range(2,data):
#         for v in range(2,data):
#             if prime_lst[j] == True and prime_lst[v] == True:
#                 if j + v == data:
#                     if min_data > abs(j - v):
#                         min_data = abs(j-v)
#                         data1 = j
#                         data2 = v

#     print(data1, data2)



#https://www.acmicpc.net/board/view/146762 - 댓글 참고
#어떤 짝수 N이 두 숫자의 합으로 나뉠 때, 두 수의 차가 가장 적고 소수이려면
#(N/2 -1)과 (N/2 +1) -> (N/2 -2)과 (N/2 +2) -> . . . 이런식으로 흘러가야 함

for i in range(time):
    input_data = int(input()) #입력받을 데이터
    
    minus_data = 0 #input_data/2 에 더하고 뺄 값
    while(True):
        if prime_lst[int(input_data/2 - minus_data)] == True and prime_lst[int(input_data/2 + minus_data)] == True:
            print(int(input_data/2 - minus_data), int(input_data/2 + minus_data))
            break

        minus_data += 1