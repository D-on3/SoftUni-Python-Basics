# На първия ред е месецът - May, June, July, August, September или October;
month = input()
# На втория ред е броят на нощувките - цяло число.
number_of_nights = int(input())
price_studio = 0
price_apartament = 0
discount_studio = 0
discount_apartment = 0

if month == 'May' or month == 'October':
    price_studio = 50
    price_apartament = 65
elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apartament = 68.70
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apartament = 77
without_discount_studio = price_studio * number_of_nights
without_discount_apartament = price_apartament * number_of_nights
# За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
if 7 > number_of_nights < 14 and month == 'May' or month == 'October':
    discount_studio = without_discount_studio * 0.05
elif 7 < number_of_nights > 14 and month == 'May' or month == 'October':
    discount_studio = without_discount_studio * 0.3
elif 7 < number_of_nights > 14 and month == 'June' or month == 'September':
    discount_studio = without_discount_studio * 0.2
if number_of_nights > 14:
    discount_apartment = without_discount_apartament * 0.1

total_price_studio = without_discount_studio - discount_studio
total_price_apartment = without_discount_apartament - discount_apartment
if month == 'May' or month == 'June' or month == 'July' or month == 'August' or month == 'September' or month == 'October':
    print(f'Apartment: {total_price_apartment:.2f} lv.')
    print(f'Studio: {total_price_studio:.2f} lv.')
