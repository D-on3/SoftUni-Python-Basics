price_for_trip = float(input())
available_money = float(input())
saved_money = 0
saved_money += available_money
counter_spend = 0
day_counter = 0
do_we_have_money_for_trip = False
type_of_command = ''
amount = 0
while price_for_trip >= saved_money:
    type_of_command = input()
    amount = float(input())
    day_counter += 1
    if type_of_command == 'spend':
        counter_spend += 1
        saved_money -= amount
        if saved_money < 0:
            saved_money = 0
        elif counter_spend == 5:
            break
    elif type_of_command == 'save':
         counter_spend = 0
         saved_money += amount
         if price_for_trip == saved_money:
            do_we_have_money_for_trip = True
            break

if do_we_have_money_for_trip:
    print(f"You saved the money for {day_counter} days.")
elif not do_we_have_money_for_trip:
    print("You can't save the money.")
    print(f"{day_counter}")
