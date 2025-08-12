from collections import deque
import sys
input = sys.stdin.readline

#입력
    #1. N: 입력할 단어의 갯수
    #2. [word] (N줄): 영어 단어

#실행
    #1. 영어 단어는 소문자로만 이루어져 있다.
    #2. 입력된 문자열은 아래 조건에 따라 정렬한다.
        #2-1. 길이가 짧은 것 부터 정렬한다.
        #2-2. 길이가 같은 문자열은 사전 순으로 정렬한다.
    #3. 중복되는 문자열은 하나만 출력한다.

#출력
    #1. 실행 조건에 맞도록 단어를 정렬하여 출력한다.

N = int(input())

word_lst = [set() for _ in range(51)] #index= 0 ~ 50 -> 문자열 길이는 50 이하
for i in range(N):
    input_data = str(input().rstrip())
    length = len(input_data)

    word_lst[length].add(input_data)

for idx in range(1, 51):
    if len(word_lst[idx]) == 0:
        continue

    elif len(word_lst[idx]) == 1:
        print(*word_lst[idx])

    else:
        word_lst[idx] = list(word_lst[idx])
        word_lst[idx].sort()
        
        for word in word_lst[idx]:
            print(word)
