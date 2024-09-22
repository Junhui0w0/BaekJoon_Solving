from sys import stdin

N = int(stdin.readline())
sangeun = set(map(int, stdin.readline().split())) #2번째 줄

#print(sangeun) #디버깅

M = int(stdin.readline())
card = list(map(int, stdin.readline().split())) #4번째 줄

ans = []
for i in card:
    if i in sangeun:
        ans.append(1)
    else:
        ans.append(0)

print(*ans[0:]) 
#ans += ans~~ 하는게 더 효율적이라면서 왜 시간초과뜸?
#list append 시간이 더 적게 듬;