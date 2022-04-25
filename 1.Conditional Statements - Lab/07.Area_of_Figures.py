choose_a_type= input().lower()
side_a = float(input())
if choose_a_type == 'square':
    pass
elif choose_a_type == 'circle':
    pass
else:
    side_b = float(input())
if choose_a_type == 'square':
    area= side_a * side_a
    print(f'{area:.3f}')
elif choose_a_type == 'rectangle':
    area = side_a * side_b
    print(f'{area:.3f}')
elif choose_a_type == 'circle':
    pi = 3.141583333333333
    radius = side_a
    area = pi * radius * radius
    print(f'{area:.3f}')
elif choose_a_type == 'triangle':
    area = side_a * side_b / 2
    print(f'{area:.3f}')