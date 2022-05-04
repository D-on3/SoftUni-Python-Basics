# Всеки кашон е с точни размери:  1m x 1m x 1m.

width_place= int(input())
lenght_place= int(input())
height_place = int(input())
full_area_place = width_place * lenght_place * height_place
place_filled = 0
command = ''
is_the_place_full = False
while command != 'Done':
    command = input()
    if command != 'Done':
        command = int(command)
        place_filled += command
        if place_filled > full_area_place:
            is_the_place_full = True
            break

if is_the_place_full:
    diffrence = abs(full_area_place - place_filled)
    print(f"No more free space! You need {diffrence} Cubic meters more.")
else:
    difference = abs(full_area_place- place_filled)
    print(f"{difference} Cubic meters left.")