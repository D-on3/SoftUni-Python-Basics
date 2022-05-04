number = int(input())
current = 1
is_current_number_than_n = False

for rows in range(1,number +1):
    for col in range(1,rows +1):
        if current > number:
            is_current_number_than_n = True
            break
        print(str(current) + ' ', end= '')
        current += 1
    if is_current_number_than_n:
        break
    print()