number_of_cats = int(input())
total_food = 0
group1= 0
group2= 0
group3= 0

for cat in range(number_of_cats):
    food_eaten = int(input())
    if 0 < food_eaten >= 100:
        total_food += food_eaten
        if 100 <= food_eaten <200:
            group1 += 1
        elif 200 <= food_eaten <300:
            group2 += 1
        elif 300 <= food_eaten <400:
            group3 += 1
total_food = total_food /1000
print(total_food)
total_calc = (total_food * 12.45)
total_calc = round(total_calc,3)
print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {total_calc:.2f} lv.")