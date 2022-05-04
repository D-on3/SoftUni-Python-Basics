cake_lenght = int(input())
cake_height = int(input())
pieces_counter = 0
is_there_cake_eaten = False
amount_of_cake = cake_height * cake_lenght
cake_served = 0
command_input = ''
while command_input != 'STOP':
    command_input = input()
    if command_input != 'STOP':
        command_input = int(command_input)
        cake_served += command_input
    if amount_of_cake < cake_served:
        is_there_cake_eaten = True
        break

if is_there_cake_eaten:
    diffrence = abs(amount_of_cake-cake_served)
    print(f"No more cake left! You need {diffrence} pieces more.")
else:
    cake_left = abs(cake_served - amount_of_cake)
    print(f"{cake_left} pieces are left.")
