operation = True

while operation:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    operator = input('Input an operator(+, -, * and /): ')

    if operator == '+':
        print(num1+num2)
    elif operator == '-':
        print(num1-num2)
    elif operator == '*':
        print(num1*num2)
    elif operator == '/':
        print(num1/num2)
    else:
        print('Invalid operator')

    yes_or_no = input('Continue? (y/n): ')
    if yes_or_no == 'n':
        operation = False
