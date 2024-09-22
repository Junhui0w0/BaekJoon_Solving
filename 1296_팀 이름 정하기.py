from collections import *
name = str(input()) #연두 영어 이름
c = Counter(name)

L = c['L']
O = c['O']
V = c['V']
E = c['E']

team_lst = list()
score_lst = list()
n = 0

def Score(Team_name):
    global team_lst
    global score_lst
    global n
    global L,O,V,E

    new_L = L
    new_O = O
    new_V = V
    new_E = E

    c = Counter(Team_name)
    new_L += c['L']
    new_O += c['O']
    new_V += c['V']
    new_E += c['E']


    team_lst.append(Team_name)
    total =((new_L+new_O) * (new_L+new_V) * (new_L+new_E) * (new_O+new_V) *
             (new_O+new_E) * (new_V+new_E)) % 100
    score_lst.append(total)
    return 0


num = int(input()) #팀 이름 후보 개수
for i in range(num):
    team_name = str(input())
    Score(team_name)

printer_lst = list()
max_data = max(score_lst)
for i in range(len(score_lst)):
    if(score_lst[i] == max_data):
        printer_lst.append(team_lst[i])

print(min(printer_lst))