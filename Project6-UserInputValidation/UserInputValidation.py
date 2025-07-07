import pyinputplus as pyip

while True:
    first_name = pyip.inputStr('Enter your first name: ')
    last_name = pyip.inputStr('Enter your last name: ')
    age = pyip.inputNum('Enter your age: ')
    email = pyip.inputEmail('Enter your email: ')
    password = input('Enter your password: ')


    print(f'\nYour Name is: {first_name} {last_name}')
    print(f'Your Age is: {age}')
    print(f'Your Email is: {email}')

    if age < 18:
        print('You are not eligible.')

    if password.strip() =='123456789':
        print("Your signed In")
    else:
        print("Your password is wrong")

    question = pyip.inputYesNo('Do you want to continue: (yes/no): ' )
    if question == 'no':
        print("Thanks for response")
        break
