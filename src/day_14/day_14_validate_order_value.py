def validate_order_value(order_value):
    errors = []
    if order_value is None:
        errors.append('Błąd, nie ma wartości zamówienia')
    elif order_value <= 0:
        errors.append('Wartość zamówienia jest mniejsza bądź równa zero')
    return errors

# Testowanie (Punkt 6)
print("Test dla poprawnej wartości:")
print(validate_order_value(123))       # Zwróci []

print("\nTest dla ujemnej wartości:")
print(validate_order_value(-50))       # Zwróci ['Wartość zamówienia jest mniejsza bądź równa zero']

print("\nTest dla braku wartości (None):")
print(validate_order_value(None))      # Zwróci ['Błąd, nie ma wartości zamówienia']