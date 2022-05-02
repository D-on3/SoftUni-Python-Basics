import math

age_of_lilly = int(input())
price_of_wash = float(input())
price_of_toy = int(input())
toys= 0
total_sum_money = []
for age in range(age_of_lilly+1):
    if age % 2 == 0 :
        total_sum_money.append(age * 10/2)
    if age % 2 !=0:
        toys += 1
total_money = sum(total_sum_money) - (age/2)
toys_income = toys * price_of_toy
total_money += toys_income
total_money = math.ceil(total_money)
if total_money >= price_of_wash:
    money_left = total_money- price_of_wash
    print(f"Yes! {money_left:.2f}")
elif total_money < price_of_wash :
    difference = price_of_wash - total_money
    print(f'No! {difference:.2f}')
