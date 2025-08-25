from collections import deque
import sys
input = sys.stdin.readline

#입력
    #1. L, C -> L: 출력될 수 있는 암호의 총 길이 / C: 암호에 사용할 수 있는 알파벳 갯수
    #2. [...] (C개): 영어 알파벳

#실행
    #1. 암호는 서로 다른 알파벳으로 구성되어 있어야 한다.
    #2. 암호는 한 개의 모음과 최소 두 개의 자음으로 구성되어 있다.
    #3. 암호는 사전순으로 정렬되어 있다.

#출력
    #1. 사용 가능한 암호를 모두 출력한다.

L, C = map(int, input().rstrip().split())
alphabet_lst = list(map(str, input().rstrip().split()))
alphabet_lst.sort()

moeum_set = set()
moeum_set.add('a')
moeum_set.add('e')
moeum_set.add('i')
moeum_set.add('o')
moeum_set.add('u')

tmp = ''
answer = ''

def DFS(index, moeum_cnt):
    global tmp, answer

    if len(tmp) == L: #길이가 L인가?
        if moeum_cnt >= 1: #모음이 1개 이상 있는가?
            if L - moeum_cnt >= 2: #자음이 2개 이상이 있는가?
                if tmp in answer:
                    return True
                
                answer += tmp + '\n'
            
        return True
    
    for i in range(index, C):
        tmp += alphabet_lst[i]

        if alphabet_lst[i] in moeum_set:
            DFS(i+1, moeum_cnt+1)

        else:
            DFS(i+1, moeum_cnt)

        tmp = tmp[:len(tmp)-1]

DFS(0, 0)
print(answer)