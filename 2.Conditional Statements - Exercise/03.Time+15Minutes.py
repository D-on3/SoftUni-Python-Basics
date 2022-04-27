hours = int(input())
minute = int(input())
minute += 15
if minute > 59:
    minute -= 60
    hours += 1
if hours > 23:
    hours -= 24

if minute < 10:
    print(f'{hours}:0{minute}')
else:
    print(f'{hours}:{minute}')