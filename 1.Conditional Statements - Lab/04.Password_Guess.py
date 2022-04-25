user_input = input()
password = ("s3cr3t!P@ssw0rd")

if user_input != password:
    print('Wrong password!')
elif user_input == password:
    print('Welcome')
