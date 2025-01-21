# app/utils/validators.py

def validate_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False

def validate_date(date_str):
    from datetime import datetime
    try:
        datetime.strptime(date_str, "%yyyy-MM-dd")
        return True
    except ValueError:
        return False