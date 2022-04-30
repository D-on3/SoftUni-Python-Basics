
city = input()
sales_volume = float(input())

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        sales_volume *= 0.05
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif 500 < sales_volume <=1000:
        sales_volume *= 0.07
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif 1000 < sales_volume <= 10000:
        sales_volume *= 0.08
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif sales_volume > 10000:
        sales_volume *= 0.12
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    else:
        print('error')
elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        sales_volume *= 0.045
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif 500 < sales_volume <=1000:
        sales_volume *= 0.075
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif 1000 < sales_volume <= 10000:
        sales_volume *= 0.10
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif sales_volume > 10000:
        sales_volume *= 0.13
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    else:
        print('error')
elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        sales_volume *= 0.055
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif 500 < sales_volume <=1000:
        sales_volume *= 0.08
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif 1000 < sales_volume <= 10000:
        sales_volume *= 0.12
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif sales_volume > 10000:
        sales_volume *= 0.145
        sales = round(sales_volume, 3)
        print(f'{sales:.2f}')
    elif sales_volume < 0:
        print('error')
elif city not in 'Sofia Plovdiv Varna':
    print('error')