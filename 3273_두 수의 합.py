from collections import deque
import sys
input = sys.stdin.readline

#입력
    #1. n: 수열의 크기
    #2. [...] (n개): 입력 데이터
    #3. x: 두 수를 합하여 만족해야할 값

#실행
    #1. 입력 데이터는 서로 다른 값이다. (즉, 중복되는 값이 없다.)
        #1-1. 이는, a+b일 때 a가 x//2보다 크거나 같은 경우 절대로 만들 수 없다.
    #2. 식은 a + b 로 단 두개의 값만을 더해서 x의 값을 만들어내야 한다.

#출력
    #1. x 값을 만들기 위해 필요한 데이터 쌍의 수를 출력한다.

n = int(input())

data_lst = list(map(int, input().rstrip().split()))
# data_lst.sort()

x = int(input())

lower_center = []
bigger_center = []

if x % 2 == 0:
    for data in data_lst:
        if data > x//2:
            bigger_center.append(data)

        elif data < x//2:
            lower_center.append(data)

else:
    for data in data_lst:
        if data > x//2:
            bigger_center.append(data)

        elif data <= x//2:
            lower_center.append(data)


lower_center.sort()
bigger_center.sort()

cnt = 0

for low in lower_center:
    for big in bigger_center:
        if low + big > x:
            break

        elif low + big == x:
            cnt += 1
            break

print(cnt)