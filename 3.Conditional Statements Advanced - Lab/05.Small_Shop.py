type_of_product = input()
city = input()
number_of_products = float(input())
price = 0

if  city == 'Sofia':
    if type_of_product == 'coffee' :
        product = 0.50
        price = number_of_products * product
        print(round(price, 2))
    elif type_of_product == 'water':
        product = 0.8
        price = number_of_products * product
        print(round(price, 2))
    elif type_of_product == 'beer':
        product = 1.20
        price = number_of_products * product
        print(round(price, 2))
    elif type_of_product == 'sweets':
        product = 1.45
        price = number_of_products * product
        print(price)
    elif type_of_product == 'peanuts':
        product = 1.60
        price = number_of_products * product
        print(round(price, 2))
elif city == 'Plovdiv':
    if type_of_product == 'coffee':
        product = 0.40
        price = number_of_products * product
        print(price)
    elif type_of_product == 'water':
        product = 0.70
        price = number_of_products * product
        print(price)
    elif type_of_product == 'beer' :
        product = 1.15
        price = number_of_products * product
        print(round(price, 2))
    elif type_of_product == 'sweets' :
        product = 1.30
        price = number_of_products * product
        print(round(price, 2))
    elif type_of_product == 'peanuts':
        product = 1.50
        price = number_of_products * product
        print(round(price, 2))
elif city == 'Varna':
    if type_of_product == 'coffee':
        product = 0.45
        price = number_of_products * product
        print(round(price, 2))
    elif type_of_product == 'water':
        product = 0.70
        price = number_of_products * product
        print(round(price, 2))
    elif type_of_product == 'beer':
        product = 1.10
        price = number_of_products * product
        print(round(price, 2))
    elif type_of_product == 'sweets':
        product = 1.35
        price = number_of_products * product
        print(round(price, 5))
    elif type_of_product == 'peanuts':
        product = 1.55
        price = number_of_products * product
        print(round(price, 2))