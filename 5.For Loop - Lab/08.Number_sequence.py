number_of_numbers = int(input())
flist = [ ]
for i in range(number_of_numbers):
    values = int(input())
    flist.append(values)

print(f'Max number: {max(flist)}')
print(f'Min number: {min(flist)}')
