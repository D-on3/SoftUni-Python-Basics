# N1 - цяло число;
number1 = int(input())
# N2 - цяло число;
number2 = int(input())
# Оператор - един символ измежду: "+", "-", "*", "/", "%".
operator = input()
calculated = 0
even_or_odd = ''
error = ''
if operator == "+":
    calculated = number1 + number2
elif operator == '-':
    calculated = number1 - number2
elif operator == "*":
    calculated = number1 * number2

if operator == '+' or operator == '-' or operator == '*':
    if calculated % 2 == 0:
        even_or_odd = 'even'
    elif calculated % 2 != 0:
        even_or_odd = 'odd'
    print(f"{number1} {operator} {number2} = {calculated} - {even_or_odd}")

if operator == '/':
    if number2 != 0:
        calculated = number1 / number2
        print(f"{number1} / {number2} = {calculated}")

if operator == '%':
    if number2 != 0:
        calculated = number1 % number2
        print(f"{number1} % {number2} = {calculated}")

if operator == '/' or operator == '%':
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
        try:
            pass
        except ZeroDivisionError:
            pass
