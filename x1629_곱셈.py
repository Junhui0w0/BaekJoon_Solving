#분할 정복을 이용한 거듭제곱 연산
#[출처] 분할 정복을 이용한 거듭제곱 연산|작성자 서동연

#지수가 짝수인 경우
    #-> C^N = C^(N/2) * C^(N/2)
#지수가 홀수인 경우
    #-> C^N = C^((N-1)/2) * C^((N-1)/2) * C
 
#이걸 왜 알아야하죠 ? . . . 시간복잡도가 O(N) -> O(logN)

from collections import deque
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

a,b,c = map(int, input().rstrip().split())

total = 1
# jisu_holsu = 0 #지수가 홀수인 경우 곱할 변수

def func(mit, jisu):
    global total
    if jisu == 1:
        total = total * mit
        return total
    
    if jisu % 2 == 0: #지수가 짝수인 경우
        jisu = jisu // 2
    
    else:
        jisu = (jisu-1) // 2
        total = total * mit
        # jisu_holsu += 1

    # jisu_holsu += 1
    total = total * mit
    a = func(mit, jisu) * func(mit, jisu)


    if a != False:
        return total
    
    return False

total = func(a,b) * a
print(total % c)
# print((a ** b) % c)
# print(jisu_holsu)