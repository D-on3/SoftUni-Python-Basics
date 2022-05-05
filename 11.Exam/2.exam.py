import math


# На първия ред е широчината на кораба - реално число в интервала [1.00... 10.00]
width_ship =  float(input()) * 10
# На втория ред е  дължината на кораба - реално число в интервала [1.00…10.00]
lenght_ship = float(input()) * 10
# На третия ред е височината на кораба - реално число в интервала [1.00…20.00]
height_ship = float(input()) * 10
# На четвъртия ред е средната височина на астронавтите  -  реално число в интервала [1.50 … 1.90]
average_height_astr= float(input())

total_volume = width_ship * lenght_ship * height_ship

one_room = 2*2*(average_height_astr+0.40)

calc = math.floor(total_volume/one_room/1000)

if 3 <= calc <= 10:
    print(f'The spacecraft holds {calc} astronauts.')
elif calc < 3:
    print("The spacecraft is too small.")
elif calc > 10:
    print("The spacecraft is too big.")
else:
    pass
