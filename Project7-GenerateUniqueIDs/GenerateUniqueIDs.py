import time
import random
import string
import csv
import uuid
import pyinputplus as pyip

with open('user_data.csv', mode='a+', newline='') as file:
    writer = csv.writer(file)
    file.seek(0)
    if not file.read(1):
        customer_id = str(uuid.uuid4())
        writer.writerow(['First Name', 'Last Name', 'Age', 'Email', 'Password', 'Customer_id'])

    while True:
        first_name = pyip.inputStr('Enter your first name: ')
        last_name = pyip.inputStr('Enter your last name: ')
        age = pyip.inputNum('Enter your age: ')
        email = pyip.inputEmail('Enter your email: ')
        password = input('Enter your password: ')

        print(f'\nYour Name is: {first_name} {last_name}')
        print(f'Your Age is: {age}')
        print(f'Your Email is: {email}')


        def generate_custom_id():
            timestamp = str(int(time.time()))
            random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            return f"ID-{timestamp}-{random_chars}"


        custom_id = generate_custom_id()
        print(f'Your id: ', custom_id)

        writer.writerow([first_name, last_name, age, email, password, custom_id])

        question = pyip.inputYesNo('Do you want to continue? (yes/no): ')
        if question == 'no':
            print(f'Your data stored')
            break

file.close()
