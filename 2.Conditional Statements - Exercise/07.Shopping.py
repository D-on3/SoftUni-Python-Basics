#Бюджетът на Петър - реално число в интервала [1.0…100000.0]
budget = float(input())
#Броят видеокарти - цяло число в интервала [1…100]
number_gpu = int(input())
#Броят процесори - цяло число в интервала [1…100]
number_cpu = int(input())
#Броят рам памет - цяло число в интервала [1…100]
number_ram = int(input())

#Видеокарта – 250 лв./бр.
total_price_gpu = number_gpu * 250
#Процесор – 35% от цената на закупените видеокарти/бр.
total_price_cpu =  (total_price_gpu * 0.35) * number_cpu
#Рам памет – 10% от цената на закупените видеокарти/бр.
total_price_ram = (total_price_gpu * 0.1) * number_ram
total_price = total_price_gpu + total_price_cpu + total_price_ram
#Ако броя на видеокартите е по - голям от този на
#процесорите получава 15 % отстъпка от крайната сметка
if number_gpu > number_cpu :
    total_price = total_price - (total_price * 0.15)

if total_price <= budget:
    left_funds = budget - total_price
    print(f"You have {left_funds:.2f} leva left!")
elif total_price > budget:
    needed = total_price - budget
    print(f"Not enough money! You need {needed:.2f} leva more!")
