number_of_tabs = int(input())
paycheck = int(input())
penalty = 0
for site in range(number_of_tabs):
    current_site = input()
    if current_site == 'Facebook':
        penalty += 150
    elif current_site == 'Instagram':
        penalty += 100
    elif current_site == 'Reddit':
        penalty += 50
if paycheck <= penalty:
    diffrence = abs(penalty - paycheck)
    print('You have lost your salary.')
elif paycheck > penalty:
    paycheck_left = int(paycheck - penalty)
    print(paycheck_left)