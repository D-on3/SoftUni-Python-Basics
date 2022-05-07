
food_in_kg = int(input()) * 1000
total_food = 0
food_left = True
comand = input()
while comand != 'Adopted':
    food = 0
    food = int(comand)
    total_food += food

    if total_food > food_in_kg:
        food_left = False

    comand = input()

if food_left:
    diffrence = food_in_kg - total_food
    print(f"Food is enough! Leftovers: {diffrence:2.} grams.")
else:
    diffrence = total_food - food_in_kg
    print(f"Food is not enough. You need {diffrence} grams more.")