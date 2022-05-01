number_range= int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(number_range):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

total_p = p1 + p2 + p3 + p4 + p5
p1_calc = (p1 / total_p) * 100
p2_calc = (p2 / total_p) * 100
p3_calc = (p3 / total_p) * 100
p4_calc = (p4 / total_p) * 100
p5_calc = (p5 / total_p) * 100

print(f'{p1_calc:.2f}%')
print(f'{p2_calc:.2f}%')
print(f'{p3_calc:.2f}%')
print(f'{p4_calc:.2f}%')
print(f'{p5_calc:.2f}%')



