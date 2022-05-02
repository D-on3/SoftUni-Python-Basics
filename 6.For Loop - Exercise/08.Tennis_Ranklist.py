# Брой турнири, в които е участвал – цяло число в интервала [1…20]
number_of_tornaments = int(input())
# Начален брой точки в ранглистата - цяло число в интервала [1...4000]
starting_points = int(input())
total_points = 0
count_win = 0
counter = 0
for tournament in range(number_of_tornaments):
    current_tournament = input().upper()
    counter += 1
    if current_tournament == 'W':
        total_points += 2000
        count_win += 1
    elif current_tournament == 'F':
        total_points += 1200
    elif current_tournament == 'SF':
        total_points += 720
total_calculated_points = starting_points + total_points
percent_calc = count_win / counter * 100

average_points = total_points // number_of_tornaments

print(f'Final points: {total_calculated_points}')
print(f'Average points: {average_points}')