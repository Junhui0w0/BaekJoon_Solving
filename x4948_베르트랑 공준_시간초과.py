from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

while(True):
    input_data = int(input().rstrip()) #입력받을 데이터
    
    if input_data == 0:
        break #0이라면 반복 취소

    s = set()

    print_data = input_data #input_data ~ 2*input_data 사이의 데이터 총 갯수
    
    for i in range(2, int((2*input_data)**0.5)+1):
        for j in range(2*i, 2*input_data+1, i):
            if input_data < j <= 2*input_data:
                s.add(j)

    print_data = print_data - len(s)


    print(print_data)