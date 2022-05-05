import math
to_the_moon = 384400 * 2
speed = int(input())
liters_of_fuel = float(input())

going = to_the_moon / speed
going = math.ceil(going)
going += 3
fuel = liters_of_fuel * to_the_moon /100
fuel = int(fuel)
print(going)
print(fuel)