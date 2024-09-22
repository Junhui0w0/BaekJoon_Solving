from sys import stdin

n = int(stdin.readline())
n_lst = set(stdin.readline().split())

#print(n_lst) #디버깅

m = int(stdin.readline())
m_lst = stdin.readline().split()

ans = ''
for data in m_lst:
    if(data in n_lst):
        ans = ans + '1\n'
    else:
        ans = ans + '0\n'

print(ans)