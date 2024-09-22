from sys import stdin

N = int(stdin.readline())

#push X // pop // size // empty // top

lst = []
ans = ''

for i in range(N):
    command = stdin.readline().split()
    if(len(command) == 2):
        lst.append(command[1])

    else:
        if(command[0] == 'pop'):
            if(len(lst) == 0):
                ans = ans + '-1\n'
            else:
                ans = ans +lst[-1] + '\n'
                lst.pop()
        
        elif(command[0] == 'size'):
            ans = ans + str(len(lst)) + '\n'

        elif(command[0] == 'empty'):
            if(len(lst) == 0):
                ans = ans + '1\n'
            else:
                ans = ans + '0\n'
        elif(command[0] == 'top'):
            if(len(lst) == 0):
                ans = ans + '-1\n'
            else:
                ans = ans + lst[-1] +'\n'
        else:
            continue

print(ans)