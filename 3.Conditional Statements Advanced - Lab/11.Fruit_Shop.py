type_of_fruits = input()
day_of_week = input()
number_of_fruits = float(input())
price = 0
if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' \
    or day_of_week == 'Friday':
    if type_of_fruits == 'banana':
        price = 2.50
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'apple':
        price = 1.20
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'orange':
        price = 0.85
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'grapefruit':
        price = 1.45
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'kiwi':
        price = 2.70
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'pineapple':
        price = 5.50
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'grapes':
        price = 3.85
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits not in 'banana apple orange grapefruit kiwi pineapple grapes':
        print('error')

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if type_of_fruits == 'banana':
        price = 2.70
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'apple':
        price = 1.25
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'orange':
        price = 0.9
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'grapefruit':
        price = 1.6
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'kiwi':
        price = 3.00
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'pineapple':
        price = 5.60
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits == 'grapes':
        price = 4.20
        price *= number_of_fruits
        print(f'{price:.2f}')
    elif type_of_fruits not in 'banana apple orange grapefruit kiwi pineapple grapes':
        print('error')

elif day_of_week not in 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday':
    pass
elif  day_of_week == 'Workday':
    pass
elif day_of_week == 'Nineday':
    pass
elif type_of_fruits == 'water':
    pass