number = int(input())

for power_off in range(number+1):
    var = 2

    if power_off % 2 == 0:
        var **= power_off
        print(var)
