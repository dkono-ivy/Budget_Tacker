# validation.py

def is_non_empty_string(s):
    """Check if the input is a non-empty string."""
    return isinstance(s, str) and bool(s.strip())

def is_float(value):
    """Attempt to convert value to float and return True if successful."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_expense(name, amount):
    """Validate expense details."""
    errors = []
    if not is_non_empty_string(name):
        errors.append("Expense name must be a non-empty string.")
    if not is_non_empty_string(amount) or not is_float(amount):
        errors.append("Expense amount must be a number.")
    return errors
