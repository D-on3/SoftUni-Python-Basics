# Бюджет - реално число;
budget = float(input())
# Един от двата възможни сезона - "summer” или "winter”.
season = input().capitalize()
#season =
destination = ''
type_of_vacation = ''
cost = 0
# При 100 лв. или по-малко - някъде в България:
if budget <= 100:
    destination = 'Bulgaria'
    # Лято - 30% от бюджета;
    if season == 'Summer':
        cost = budget * 0.3
        type_of_vacation = 'Camp'
    elif season == 'Winter':
        cost = budget * 0.7
        type_of_vacation = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'Summer':
        cost = budget * 0.4
        type_of_vacation = 'Camp'
    elif season == 'Winter':
        cost = budget * 0.8
        type_of_vacation = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    type_of_vacation = 'Hotel'
    cost = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {cost:.2f}")