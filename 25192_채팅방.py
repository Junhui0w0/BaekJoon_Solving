from sys import stdin

N = int(stdin.readline())

total = 0
for i in range(N):
    chat = stdin.readline().rstrip() #채팅 내용 입력받기
    if(chat == 'ENTER'):
        #print('true') #디버깅
        user_set = set()
    else:
        if(chat in user_set):
            continue
        else:
            user_set.add(chat)
            total += 1

print(total)