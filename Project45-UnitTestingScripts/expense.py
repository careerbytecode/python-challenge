def calculate_total(expenses):
    total = 0
    for item in expenses:
        total += item['amount']
    return total

def calculate_total_by_category(expenses, category=None):
    total = 0
    for item in expenses:
        if category is None or item['category'] == category:
            total += item['amount']
    return total

