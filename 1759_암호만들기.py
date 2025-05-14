from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

L, C = map(int, input().rstrip().split()) #L=암호 최대 길이 / C=입력가능한 문자
lst = list(map(str, input().rstrip().split())) #C개의 문자를 담을 List
lst.sort()

moeum = set()
moeum.add('a')
moeum.add('e')
moeum.add('i')
moeum.add('o')
moeum.add('u')

def DFS(start_index, length, string, moeum_length):
    if length == L:
        if moeum_length >= 1 and length - moeum_length >= 2:
            print(string)
            return 1
    
    for i in range(start_index, C):
        if visited[i] == True:
            continue

        if visited[i] == False:
            visited[i] = True

            if lst[i] in moeum:
                DFS(i, length+1, string+lst[i], moeum_length+1)
            
            else:
                DFS(i, length+1, string+lst[i], moeum_length)

            visited[i]=False

    return 1

for i in range(C):
    if C-i == L-1:
        break

    visited = [False] * C
    visited[i] = True
    moeum_length=0

    if lst[i] in moeum:
        moeum_length = 1

    DFS(i, 1, lst[i], moeum_length)