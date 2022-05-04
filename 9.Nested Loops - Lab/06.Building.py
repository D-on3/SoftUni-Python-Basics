floors = int(input())
numbers_of_rooms = int(input())
room_numbers = ''

for f in range(floors,0,-1):
    for r in range(numbers_of_rooms):
        current_room = f * 10 + r
        if f == floors:
            print(f'L{current_room} ', end='')

        elif f % 2 != 0:
            room_numbers += f'A{current_room} '

        else:
            room_numbers += f'O{current_room} '


    print(room_numbers)
    room_numbers = ''