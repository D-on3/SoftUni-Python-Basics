groups_climbers = int(input())
total_climbers = 0
climbers_musala = 0
climbers_monblan = 0
climbers_kili = 0
climbers_k2 = 0
climbers_everest = 0
number_of_climbers = 0
for climbers in range(groups_climbers):
    number_of_climbers = int(input())
    total_climbers += number_of_climbers
    if number_of_climbers <= 5:
        climbers_musala += number_of_climbers
    elif 6 <= number_of_climbers <= 12:
        climbers_monblan += number_of_climbers
    elif 13 <= number_of_climbers <= 25:
        climbers_kili += number_of_climbers
    elif 26 <= number_of_climbers <= 40:
        climbers_k2 += number_of_climbers
    elif 40 < number_of_climbers >= 41:
        climbers_everest += number_of_climbers

percents_calc_musala =  (climbers_musala / total_climbers) * 100
percents_calc_monblan = (climbers_monblan / total_climbers) * 100
percents_calc_kili =  (climbers_kili / total_climbers) * 100
percents_calc_k2 =  (climbers_k2 / total_climbers) * 100
percents_calc_everest = (climbers_everest / total_climbers) * 100

print(f'{percents_calc_musala:.2f}%')
print(f'{percents_calc_monblan:.2f}%')
print(f'{percents_calc_kili:.2f}%')
print(f'{percents_calc_k2:.2f}%')
print(f'{percents_calc_everest:.2f}%')