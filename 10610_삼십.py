from sys import stdin

N = stdin.readline().rstrip() #입력받을 수
lst = list(N)
lst.sort(reverse=True)
# print(lst) #디버깅
# print(lst[-1]) #디버깅

total = 0
if(lst[-1] == '0'):
    for i in lst:
        total = total + int(i)
    if(total % 3 == 0):
        print(*lst,sep='')
    else:
        print('-1')
else:
    print('-1')
