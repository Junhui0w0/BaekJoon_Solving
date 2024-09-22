ans = ''

num = int(input()) #시행 횟수

def func(N,M):
    N_total = 1
    M_total = 1
    total = 1

    for i in range(1, M+1):
        M_total = M_total * i #분자

    for i in range(1,N+1):
        N_total = N_total * i #분모 1

    for i in range(1,M-N+1):
        total = total * i #분모 2

    data =M_total // (N_total * total) 
    #data =M_total / N_total / total  => 실수로 나옴
        #int()로 묶어도 안됨!!!!!

    return data

for i in range(num):
    N,M = list(map(int,input().split()))
    ans = ans + str(func(N,M)) + '\n'

print(ans)