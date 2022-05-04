start_iteration = int(input())
end_of_iteration = int(input())
magic_number = int(input())
combination =  0
first_combination = 0
is_it_found = False

for n1 in range(start_iteration,end_of_iteration+1):
    for n2 in range(start_iteration,end_of_iteration+1):
        combination += 1
        if n1 + n2  == magic_number:
            is_it_found = True
            print(f"Combination N:{combination} ({n1} + {n2} = {magic_number})")
            break


    if is_it_found:
        break

if not is_it_found:
    print(f"{combination} combinations - neither equals {magic_number}")
