user_input = int(input())
if user_input <= 99:
    print('Less than 100')
elif 100 <= user_input <= 200:
    print('Between 100 and 200')
elif user_input >= 201:
    print('Greater than 200')