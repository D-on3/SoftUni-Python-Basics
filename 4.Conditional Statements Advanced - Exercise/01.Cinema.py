type_of_projection = input()
rows = int(input())
columns = int(input())
total_seats = rows * columns
price = 0

if type_of_projection == 'Premiere':
    price = 12.00
elif type_of_projection == 'Normal':
    price = 7.50
elif type_of_projection == 'Discount':
    price = 5.00
total_seats *= price
print(f'{total_seats:.2f} leva')