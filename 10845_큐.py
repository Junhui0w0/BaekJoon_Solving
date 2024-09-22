from sys import stdin
from collections import deque

N = int(stdin.readline()) #입력 줄 개수
d = deque()
ans = ''

for i in range(N):
    command = stdin.readline().split()
    if(len(command) == 2):
        d.append(command[1])
    else:
        if(command[0] == 'pop'):
            if(len(d) == 0):
                ans = ans + '-1\n'
            else:
                ans = ans + str(d.popleft()) + '\n' #출력과 동시에 삭제됨
        
        elif(command[0] == 'size'):
            ans = ans + str(len(d)) + '\n'
        
        elif(command[0] == 'empty'):
            if(len(d) == 0):
                ans = ans + '1\n'
            else:
                ans = ans + '0\n'

        elif(command[0] == 'front'):
            if(len(d) == 0):
                ans = ans + '-1\n'
            else:
                ans = ans + str(d[0]) + '\n'

        elif(command[0] == 'back'):
            if(len(d) == 0):
                ans = ans + '-1\n'
            else:
                ans = ans + str(d[-1]) + '\n'

print(ans)