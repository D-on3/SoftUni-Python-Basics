#Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
budget_film = float(input())
#Брой на статистите – цяло число в интервала [1 … 500]
number_of_statist = int(input())
#Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
number_of_dressing = float(input())
##Декорът за филма е на стойност 10% от бюджета.
calc_decore = budget_film * 0.1
sum_of_dress = number_of_statist * number_of_dressing
#При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
if number_of_statist > 150:
   sum_of_dress = sum_of_dress - (sum_of_dress * 0.1)
else:
    pass
total_price = sum_of_dress + calc_decore

if budget_film < total_price:
    print(f'Not enough money!')
    unsuffition_funds = abs (total_price - budget_film)
    print(f'Wingard needs {unsuffition_funds:.2f} leva more.')
elif budget_film >= total_price:
    print("Action!")
    sufficient_funds = budget_film - total_price
    print(f"Wingard starts filming with {sufficient_funds:.2f} leva left.")