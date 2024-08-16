import datetime


banks_data = [
    {"bank_name": "Тестовый банк 1", "debtors": [
        {"name": "Человек 1", "due_date": datetime.datetime(2024, 9, 15)},
        {"name": "Человек 2", "due_date": datetime.datetime(2024, 9, 1)}
    ]},
    {"bank_name": "Тестовый банк 2", "debtors": [
        {"name": "Человек 3", "due_date": datetime.datetime(2024, 8, 25)},
        {"name": "Человек 4", "due_date": datetime.datetime(2024, 9, 10)}
    ]}
]


def get_banks_debtors(current_date: datetime, critical_days: list) -> dict:
    """Получение должников банков"""
    banks_dict = {}
    for bank in banks_data:
        bank_name = bank["bank_name"]
        banks_dict[bank_name] = {day: [] for day in critical_days}
        
        for debtor in bank["debtors"]:
            days_left = (debtor["due_date"].date() - current_date).days
            if days_left in critical_days:
                banks_dict[bank_name][days_left].append(debtor["name"])
    return banks_dict



def main():
    critical_days = [30, 15, 5, 0]
    current_date = datetime.datetime.now().date()
    banks_dict = get_banks_debtors(current_date, critical_days)
    print(banks_dict)
    return None

if __name__ == '__main__':
    main()