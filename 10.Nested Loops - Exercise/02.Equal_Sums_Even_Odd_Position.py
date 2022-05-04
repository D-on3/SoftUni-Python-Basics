first_number = int(input())
second_number = int(input())

for current_number in range(first_number,second_number+1):
    even_num=  0
    odd_num = 0
    current_number_conv = str(current_number)

    for index,digit in enumerate(current_number_conv):
        if index % 2 == 0:
            odd_num += int(digit)
        else:
            even_num += int(digit)

    if even_num == odd_num:
        print(current_number, end= ' ')
