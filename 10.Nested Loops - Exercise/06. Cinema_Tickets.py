standard_tickets = 0
student_tickets = 0
kids_tickets = 0
total_tickets = 0

command = input()

free_spaces_saved = 0
finished = False
while command != "Finish":

    sold_tickets = 0
    free_spaces = int(input())
    free_spaces_saved = free_spaces

    while free_spaces > 0:
        type_of_ticket = input()

        if type_of_ticket == "End":
            break
        if type_of_ticket == 'student':
            student_tickets += 1
        elif type_of_ticket == 'standard':
            standard_tickets += 1
        elif type_of_ticket == 'kid':
            kids_tickets += 1
        sold_tickets += 1
        total_tickets += 1
        free_spaces -= 1
        if type_of_ticket == 'Finish':
            break
        movie = command
    calculation_salon = (sold_tickets / free_spaces_saved) * 100
    print(f"{command} - {calculation_salon:.2f}% full.")

    command = input()


print(f"Total tickets: {total_tickets}")
print(f"{student_tickets/total_tickets*100:.2f}% student tickets.")
print(f"{standard_tickets/total_tickets*100:.2f}% standard tickets.")
print(f"{kids_tickets /total_tickets*100:.2f}% kids tickets.")

