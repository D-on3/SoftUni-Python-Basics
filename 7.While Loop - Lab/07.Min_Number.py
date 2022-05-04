current_number_string = input()
list = [ ]
while True:
    if current_number_string != 'Stop':
        current_number_int=int(current_number_string)
        list.append(current_number_int)
    current_number_string = input()
    if current_number_string == 'Stop':
        print(min(list))
        break