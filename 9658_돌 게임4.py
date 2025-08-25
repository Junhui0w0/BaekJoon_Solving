import sys
input = sys.stdin.readline

n = int(input())
dp_lst = [None, 'CY', 'SK', 'CY', 'SK', 'SK', 'SK', 'SK']

if n <= 7:
    print(dp_lst[n])

else:
    if n % 7 == 0:
        print('SK')

    else:
        print(dp_lst[n%7])