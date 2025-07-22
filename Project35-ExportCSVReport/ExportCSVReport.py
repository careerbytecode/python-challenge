import csv

# data with table list and tuple, Python csv.writer() accepts both lists and tuples as row input, so mixing them works fine.
input_variable = [
    ['S.no', 'name', 'e-mail','phone no'],
    [1, 'Siva', 'siva@email.com', '63542158963'],
    [2, 'Raj', 'raj@email.com', '2345125879'],
    [3, 'Guru', 'guru@email.com','7845123698'],
    (4, 'Ravi', 'rv123@email.com','5689234578'),
    (5, 'Mani', 'mani@email.com','7598425692')
]

# Write to saved_data.csv
with open('saved_data.csv', 'w', newline='') as csvfile:
    saved_data = csv.writer(csvfile, delimiter = ',')  #delimiter is comma
    saved_data.writerows(input_variable)

print(" CSV file created successfully!")
