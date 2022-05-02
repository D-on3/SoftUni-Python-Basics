number = int(input())
number2 = 0
sum = 0
while sum <= number:
    number2 = int(input())
    sum += number2
    if sum >= number:
        print(sum)
        break