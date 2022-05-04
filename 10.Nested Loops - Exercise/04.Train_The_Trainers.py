
number_of_jury =  int(input())
current_task = input()
sum_of_grades = 0
average_grade = 0
current_grade = 0
are_we_finished = False
final_score = 0
task_counter = 0

while current_task != 'Finish':
    counter = 0
    if counter < number_of_jury:
        for grades in range(number_of_jury):
            current_grade = float(input())
            sum_of_grades += current_grade
            final_score +=  current_grade

    else:
        counter = 0
    sum_of_grades /= number_of_jury
    print(f'{current_task} - {sum_of_grades:.2f}.')
    sum_of_grades = 0

    task_counter += number_of_jury
    task_calculator = final_score / task_counter
    current_task = input()
    if current_task == 'Finish':
        are_we_finished = True
        break

if are_we_finished:
    print(f"Student's final assessment is {task_calculator:.2f}.")