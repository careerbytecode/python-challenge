from faker import Faker
import csv

fake = Faker()

x = int(input("Enter how many data records you need: "))

with open('fake_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Address', 'Email', 'DOB'])  # Header row

    for i in range(x):
        name = fake.name()
        address = fake.address()
        email = fake.email()
        date_of_birth = fake.date_of_birth()

        print(f"\nRecord {i+1}")
        print(f"Name        : {name}")
        print(f"Address     : {address}")
        print(f"Email       : {email}")
        print(f"Date of Birth: {date_of_birth}")

        writer.writerow([name, address, email, date_of_birth])

print("\n✅ Data saved to fake_data.csv")
