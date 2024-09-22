from sys import stdin
from collections import deque

n,m = stdin.readline().split()
poke_d = deque()

#tmp = []                                                                    #디버깅    

ans = ''
for i in range(int(n) + int(m)): #0 ~ 30 = 31개
    question = stdin.readline()
    if(i < int(n)): #0~25 = 26개
        poke_d.append(question) #포켓몬 도감에 저장
    else: # 26 ~ 30 = 5개
        if(65 <= ord(question[0][0]) <= 90): #만약 question의 첫글자가 A~Z 라면
            #tmp.append(ord(question[0][0]))                                 #디버깅
            ans = ans + str(int(poke_d.index(question)) + 1) + '\n'
        
        else: #그 외 정수
            ans = ans + str(poke_d[int(question) - 1]) 

print(ans)
#print(tmp) #디버깅