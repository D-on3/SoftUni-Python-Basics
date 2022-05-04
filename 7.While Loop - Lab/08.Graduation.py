name = input()
year_grade = 0
counter = 1  # започва от 1 защото ако ученикът не мине годината counter не трябва да се увеличава и класовете се движат с -1 назад
classesPassed = 0  # Брояч на минатите класове
failed = False  # Логическа променлива за проверка дали класът е минат
fail_counter = 0
while counter <= 12:
    grades = float(input())
    if grades < 4:
        fail_counter += 1
        failed = True  # Използва се в следващото условие, защото иначе counter се увеличаваше дори когато класът не е минат
    else:
        year_grade += grades
        classesPassed += 1
    if fail_counter < 2 and failed == False:
        counter += 1
    if fail_counter == 2:
        break
    failed = False  # Връщане на старата стойност на логическата променлива

if fail_counter < 2:
    year_grade = year_grade / classesPassed
    print(f'{name} graduated. Average grade: {year_grade:.2f}')
else:
    print(f'{name} has been excluded at {counter} grade')