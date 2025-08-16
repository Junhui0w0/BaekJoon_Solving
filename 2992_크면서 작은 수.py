import sys
input = sys.stdin.readline

X = int(input().rstrip())
component_lst = list(str(X))
# print(component_lst)
visited = [False] * len(component_lst)

answer = []
tmp = '0'

def DFS(index):
    global tmp

    if int(tmp) > X:
        answer.append(int(tmp))
        return True
    
    for i in range(len(component_lst)):
        if visited[i] == False:
            tmp += component_lst[i]
            visited[i] = True
            
            DFS(i+1)

            tmp = tmp[:len(tmp)-1]
            visited[i] = False

DFS(0)
if len(answer) == 0:
    print(0)

else:
    print(min(answer))