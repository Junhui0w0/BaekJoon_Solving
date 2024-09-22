data = int(input())
n = 1

origin_data = data

while True:
    ten_size = data // 10 #10의 자리
    one_size = data % 10 #1의 자리

    new_one_size = (ten_size + one_size) % 10 #새로운 숫자의 일의 자리
    new_ten_size = one_size #새로운 숫자의 10의 자리

    new_data = new_ten_size * 10 + new_one_size
    if(new_data == origin_data):
        break
    else:
        data = new_data
        n += 1

print(n)