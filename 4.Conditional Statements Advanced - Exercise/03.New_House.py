type_of_flowers = input()
# Брой цветя - цяло число;
number_of_flowers = int(input())
# Бюджет - цяло число.
budget = int(input())

roses = 5
dalias = 3.80
tulips = 2.80
narcis = 3
gladiolas = 2.50
price = 0
condition = True
if type_of_flowers == "Roses":
    if number_of_flowers > 80:
        price = roses - (roses * 0.10)
    else:
        price = roses
elif type_of_flowers == "Dahlias":
    if number_of_flowers > 90:
        price = dalias - (dalias * 0.15)
    else:
        price = dalias
elif type_of_flowers == "Tulips":
    if number_of_flowers > 80:
        price = tulips - (tulips * 0.15)
    else:
        price = tulips
elif type_of_flowers == "Narcissus":
    if number_of_flowers < 120:
        price = narcis + (narcis * 0.15)
    else:
        price = narcis
elif type_of_flowers == "Gladiolus":
    if number_of_flowers < 80:
        price = gladiolas + (gladiolas * 0.2)
    else:
        price = gladiolas
else :
    condition = False
total_price = number_of_flowers * price
if total_price < budget:
    diffrence = abs(total_price - budget)
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {diffrence:.2f} leva left.")
elif total_price > budget:
     difference = abs(budget - total_price)
     print(f"Not enough money, you need {difference:.2f} leva more.")
else :
    condition = False