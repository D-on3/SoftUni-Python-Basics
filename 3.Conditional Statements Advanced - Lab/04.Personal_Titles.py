age_input = float(input())
gender = input()

if gender == 'm':
    if age_input >= 16:
        print('Mr.')
    elif age_input < 15.999:
        print('Master')
elif gender == 'f':
    if age_input >= 16:
        print('Ms.')
    elif age_input < 15.999:
        print('Miss')