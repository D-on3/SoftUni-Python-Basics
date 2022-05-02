user_name = input()
password = input()
data = ''
cond = True
while cond:
    data = input()
    if password == data:
        print(f'Welcome {user_name}!')
        cond = False