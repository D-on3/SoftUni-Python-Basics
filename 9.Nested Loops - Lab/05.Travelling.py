sum_money = 0

while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    while budget >= sum_money:
        current_sum = float(input())
        sum_money += current_sum
        if sum_money >= budget :
            print(f"Going to {destination}!")
            sum_money = 0
            break