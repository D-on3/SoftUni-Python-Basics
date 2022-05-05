


# На първия ред - месецът - текст с възможности: "", "", "", "", "july", "august"
mount= input()
# На втория ред - броят на прекараните часове - цяло число в диапазона [1...10]
hours_in = int(input())
# На третия ред - броят на хората в групата -  цяло число в диапазона [1...10]
number_of_ppl = int(input())
# На четвъртия ред - времето от деня – текст с възможности: "day" или "night"
day_time= input()
price= 0
if mount == 'march' or mount == 'april' or mount == 'may':
    if day_time == 'day':
        price = 10.50
    elif day_time == 'night':
        price =   8.40
if mount == 'june' or mount == 'july' or mount == 'august':
    if day_time == 'day':
        price = 12.60
    elif day_time == 'night':
        price = 10.20


if number_of_ppl >= 4:
    price = price-price*0.1
if hours_in >= 5:
    price = price- price * 0.5

total_calc = price* number_of_ppl * hours_in


print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_calc:.2f}")
