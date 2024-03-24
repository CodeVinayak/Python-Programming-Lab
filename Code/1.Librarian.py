def calculate_fine(actual_date, expected_date):
    actual_day, actual_month, actual_year = actual_date
    expected_day, expected_month, expected_year = expected_date

    if actual_year > expected_year:
        return 10000
    elif actual_year == expected_year:
        if actual_month > expected_month:
            return 500 * (actual_month - expected_month)
        elif actual_month == expected_month and actual_day > expected_day:
            return 15 * (actual_day - expected_day)
    return 0

actual_return_date = (5, 8, 2023)
expected_return_date = (2, 8, 2023)
fine = calculate_fine(actual_return_date, expected_return_date)
print(f"Fine: {fine} Rupees")
