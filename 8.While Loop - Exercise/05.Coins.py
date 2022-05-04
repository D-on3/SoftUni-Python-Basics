sum_of_money = float(input())
sum = int(sum_of_money * 100)
coin_counter = 0
while True:
    coin_counter += sum // 200
    sum %= 200
    coin_counter += sum // 100
    sum %= 100
    coin_counter += sum // 50
    sum %= 50
    coin_counter += sum // 20
    sum %= 20
    coin_counter += sum // 5
    sum %= 5
    coin_counter += sum // 2
    sum %= 2
    coin_counter += sum // 1
    sum %= 1

    print(coin_counter)
    break06. Cake