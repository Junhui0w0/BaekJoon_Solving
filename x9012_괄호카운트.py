from sys import stdin

N = int(stdin.readline()) #데이터 개수
ans = ''

for i in range(N):
    oper = list(stdin.readline())

    if(oper.count('(') == oper.count(')')):
        ans = ans + 'YES\n'
    else:
        ans = ans + 'NO\n'

print(ans)