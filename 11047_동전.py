from sys import stdin

n, money = stdin.readline().split() #문자열 저장 / n = 데이터 개수 / money = 가격
coin_lst = []

for i in range(int(n)):
    coin = int(stdin.readline())
    coin_lst.append(coin)

#print(coin_lst) #디버깅
    
coin_count = 0 #코인 총 개수

for i in range(int(n)-1,-1,-1):
    coin_count += int(money) // coin_lst[i] # coin 총 개수 count
    money = int(money) % coin_lst[i]

print(coin_count)