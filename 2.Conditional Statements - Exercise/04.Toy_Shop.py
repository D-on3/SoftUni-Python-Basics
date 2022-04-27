puzzle = 2.60
talking_doll = 3
stuffed_bear = 4.10
minion = 8.20
truck = 2

# Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
price_of_trip = float(input())
# Брой пъзели - цяло число в интервала [0… 1000]
number_of_puzzles = int(input())
# Брой говорещи кукли - цяло число в интервала [0 … 1000]
number_of_talking_dolls = int(input())
# Брой плюшени мечета - цяло число в интервала [0 … 1000
number_of_stuffed_bear = int(input())
# Брой миньони - цяло число в интервала [0 … 1000]
number_of_minions = int(input())
# Брой камиончета - цяло число в интервала [0 … 1000]
number_of_truck = int(input())

total_toys = number_of_puzzles + number_of_puzzles + number_of_talking_dolls + number_of_stuffed_bear + number_of_minions + number_of_truck
price_puzzle = number_of_puzzles * puzzle
price_talking_dolls = number_of_talking_dolls * talking_doll
price_stuffed_bear = number_of_stuffed_bear * stuffed_bear
price_minions = number_of_minions * minion
price_truck = number_of_truck * truck
total_price = price_puzzle + price_talking_dolls + price_stuffed_bear + price_minions + price_truck
#Discount calculations:
if total_toys >= 50:
    total_price = total_price - (total_price * 0.25)
else:
    pass
money_left = total_price - (total_price * 0.1)
money_for_trip = money_left - price_of_trip
if money_left >= price_of_trip:
    print(f'Yes! {money_for_trip:.2f} lv left.')
elif money_left < price_of_trip:
    unsuffition_funds = price_of_trip - money_left
    print(f'Not enough money! {unsuffition_funds:.2f} lv needed.')