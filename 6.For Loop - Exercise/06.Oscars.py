name_of_actor = input()
point_acadamy = float(input())
number_of_jury= int(input())

point_given_judge = 0
total_one = 0
total_points = point_acadamy
win_points = 1250.50
for _ in range(number_of_jury):
    name_judge = input()
    points_given_judge = float(input())
    name_lenght = len(name_judge)
    total_one = (name_lenght * points_given_judge) / 2
    total_points += total_one
    if total_points >= 1250.50:
        break

if total_points >= 1250.50:
    round_total_points = round(total_points, 1)
    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {round_total_points}!')

elif total_points < 1250.50:
    diffrence = win_points - total_points
    diffrence1 = round(diffrence, 1)
    print(f'Sorry, {name_of_actor} you need {diffrence1} more!')