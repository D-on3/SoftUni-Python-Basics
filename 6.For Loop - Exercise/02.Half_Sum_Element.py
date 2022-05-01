flist = [ ]
user_input_numbers = int(input())
for number in range(user_input_numbers):
    current_number= int(input())
    flist.append(current_number)
b = max(flist)
a = flist.index(b)
del flist[a]
calc = sum(flist)
if calc == b:
    print('Yes')
    print(f'Sum = {calc}')

elif b != calc:
    difference = abs(calc - b)
    print('No')
    print(f'Diff = {difference}')03. Histogram