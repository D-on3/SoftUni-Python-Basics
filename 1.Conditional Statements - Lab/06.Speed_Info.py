speed= float(input())

if speed <= 10.:
    print('slow')
elif 10.00000001 <= speed <= 50.:
    print('average')
elif 50.00000001 <= speed <= 150.:
    print('fast')
elif 150.0000001 <= speed <= 1000.:
    print('ultra fast')
else:
    print('extremely fast')