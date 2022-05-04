sum_prime_numbers = 0
sum_non_prime_numbers = 0
is_number_prime = False
command = input()

while command != 'stop':
    current_number = int(command)
    command = input()
    if current_number < 0:
        print('Number is negative.')
    else:
        is_number_prime = True
        for number in range(2, current_number):
            if current_number % number == 0:
                is_number_prime = False
                break
        if is_number_prime:
            sum_prime_numbers += current_number
        else:
            sum_non_prime_numbers += current_number

    if command == 'stop':
        break
print(f'Sum of all prime numbers is: {sum_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_non_prime_numbers}')
