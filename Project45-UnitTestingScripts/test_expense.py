from expense import calculate_total, calculate_total_by_category

def test_calculate_total():
    data = [
        {"category": "food", "amount": 100},
        {"category": "travel", "amount": 50}
    ]
    assert calculate_total(data) == 150

def test_calculate_total_by_category():
    data = [
        {"category": "food", "amount": 100},
        {"category": "travel", "amount": 50},
        {"category": "food", "amount": 25}
    ]
    assert calculate_total_by_category(data) == 175
    assert calculate_total_by_category(data, "food") == 125
    assert calculate_total_by_category(data, "travel") == 50
    assert calculate_total_by_category(data, "misc") == 0

