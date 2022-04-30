# Бюджет на групата - цяло число;
budget = int(input())
# Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
season = input()
# Брой рибари - цяло число.
number_of_fisherman = int(input())
price = 0
discount = 0
number_discount = 0
if season == "Spring":
    price = 3000
elif season == "Summer":
    price = 4200
elif season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if number_of_fisherman <= 6:
    discount = price * 0.1
elif 7 <= number_of_fisherman <= 11:
    discount = price * 0.15
elif number_of_fisherman > 12:
    discount = price * 0.25

if number_of_fisherman % 2 == 0:
    if season != 'Autumn':
        number_discount = (price - discount) * 0.05
total_price_boat = price - discount - number_discount

if total_price_boat <= budget:
    difference = budget - total_price_boat
    print(f'Yes! You have {difference:.2f} leva left.')

elif total_price_boat > budget:
    difference = abs(budget - total_price_boat)
    print(f"Not enough money! You need {difference:.2f} leva.")