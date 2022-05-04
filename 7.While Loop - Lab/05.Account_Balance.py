bank_deposit = ''
total_sum = 0
bank_deposit_conv = 0
while True:
    bank_deposit = input()

    if bank_deposit != 'NoMoreMoney':
        bank_deposit_conv = float(bank_deposit)
        if bank_deposit_conv > 0:
            print(f'Increase: {bank_deposit_conv:.2f}')
            total_sum += bank_deposit_conv
    if bank_deposit_conv < 0 :
        bank_deposit_conv = float(bank_deposit)
        print(f'Invalid operation!')
        print(f'Total: {total_sum:.2f}')
        break
    if bank_deposit == 'NoMoreMoney':
        print(f'Total: {total_sum:.2f}')
        break
