number_of_bad_grades = int(input())
bad_grades = 0
is_failed = False
current_task = input()
last_task = ''
total_grades = 0
total_tasks = 0

while bad_grades <= number_of_bad_grades:
    grade_given = int(input())
    total_grades += grade_given
    total_tasks += 1
    if grade_given <= 4:
        bad_grades += 1
        if bad_grades == number_of_bad_grades:
            is_failed = True
            break
    last_task = current_task
    current_task = input()
    if current_task == 'Enough':
        break

if not is_failed:
     average_grade = total_grades / total_tasks
     print(f"Average score: {average_grade:.2f}")
     print(f"Number of problems: {total_tasks}")
     print(f"Last problem: {last_task}")
elif is_failed:
        print(f"You need a break, {bad_grades} poor grades.")