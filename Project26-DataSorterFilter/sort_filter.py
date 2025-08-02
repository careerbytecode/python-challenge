employees = [
    {"name": "Pankaj", "age": 29},
    {"name": "Aaruth", "age": 35},
    {"name": "Ankita", "age": 41},
    {"name": "Manoj", "age": 27}
]

older_than_30 = []
for emp in employees:
    if emp["age"] > 30:
        older_than_30.append(emp)

def get_name(employee):
    return employee["name"]

sorted_employees = sorted(older_than_30, key=get_name)

print("Employees older than 30, sorted by name:\n")
for emp in sorted_employees:
    print("Name:", emp["name"], ", Age:", emp["age"])

