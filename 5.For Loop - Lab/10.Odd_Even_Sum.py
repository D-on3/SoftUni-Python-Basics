number = int(input())

even_sum = 0
odd_sum = 0
for i in range(number):
     curent_number = int(input())

     if i % 2  == 0 :
         even_sum += curent_number
     elif i % 2 != 0:
         odd_sum += curent_number

if even_sum == odd_sum:
     total_sum = even_sum
     print('Yes')
     print(f'Sum = {total_sum}')
else:
     diffrence = abs(odd_sum-even_sum)
     print('No')
     print(f'Diff = {diffrence}')
