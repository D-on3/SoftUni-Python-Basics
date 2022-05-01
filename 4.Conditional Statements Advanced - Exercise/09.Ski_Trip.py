number_of_nights = int(input())
type_of_room = input()
command = input()
total_sum = 0
discount = 0
if type_of_room == "room for one person":
    total_sum += 18
    total_sum *= (number_of_nights - 1)
    if number_of_nights < 10:
        discount = 0
    elif 10 <= number_of_nights <= 15:
        discount = 0
    elif number_of_nights > 15:
        discount = 0

elif type_of_room == 'apartment':
    total_sum += 25
    total_sum = (number_of_nights - 1) * total_sum
    if number_of_nights < 10:
        discount = total_sum * 0.3
    elif 10 <= number_of_nights <= 15:
        discount = total_sum * 0.35
    elif number_of_nights > 15:
        discount = total_sum * 0.5

elif type_of_room == "president apartment":
    total_sum += 35
    total_sum = (number_of_nights - 1) * total_sum
    if number_of_nights < 10:
        discont = total_sum * 0.1
    elif 10 <= number_of_nights <= 15:
        discount = total_sum * 0.15
    elif number_of_nights > 15:
        discount = total_sum * 0.2

total_sum = abs(total_sum - discount)

if command == 'positive':
    total_sum = (total_sum * 0.25) + total_sum
elif command == 'negative':
    total_sum = total_sum - (total_sum * 0.1)

print(f'{total_sum:.2f}')