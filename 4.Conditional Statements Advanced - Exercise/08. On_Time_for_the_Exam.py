import math
# Първият ред съдържа час на изпита - цяло число от 0 до 23;
hour_of_exam = int(input())
# Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
minutes_of_exam = int(input())
# Третият ред съдържа час на пристигане - цяло число от 0 до 23;
hour_of_arrival = int(input())
# Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.
minutes_of_arrival = int(input())

exam_minutes = hour_of_exam * 60 + minutes_of_exam
arrival = hour_of_arrival * 60 + minutes_of_arrival
calculation = abs(exam_minutes - arrival)
calculations = exam_minutes - arrival
hours = calculation / 60
hours = math.floor(hours)
minutes = calculation % 60

if 0 <= calculations <=30:
    print("On time")
    if minutes != 0:
        print(f"{abs(minutes)} minutes before the start")
elif 30 < calculations >= 31:
    print("Early")
    if hours == 0:
        print(f"{abs(minutes)} minutes before the start")
    else:
        if minutes < 10:
            print(f"{abs(hours)}:0{abs(minutes)} hours before the start")
        else:
            print(f"{abs(hours)}:{abs(minutes)} hours before the start")
elif -60 <= calculations < 0:
    print("Late")
    print(f"{abs(minutes)} minutes after the start")
elif calculations < -61:
    print("Late")
    if minutes < 10:
        print(f"{abs(hours)}:0{abs(minutes)} hours after the start")
    else:
        print(f"{abs(hours)}:{abs(minutes)} hours after the start")
