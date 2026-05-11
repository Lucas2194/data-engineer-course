orders = [
    {
        'order_id': 101,
        'order_value': 0,
        'status': 'unpaid'
    },
    {
        'order_id': 102,
        'order_value': 0,
        'status': 'cancel'
    },
    {
        'order_id': 103,
        'order_value': 120,
        'status': 'pending'
    },
    {
        'order_value': 120,
        'status': 'sent'
    }
]

required_keys = ['order_id', 'order_value', 'status']
allowed_statuses = ['paid', 'cancel', 'pending']

errors = []

for order in orders:
    # Krok 1: Sprawdzamy brakujące klucze dla TEGO JEDNEGO zamówienia
    missing_keys = []
    for key in required_keys:
        if key not in order:
            errors.append(f"W słowniku brakuje klucza: {key}")
            missing_keys.append(key)
            
    # Krok 2: Sprawdzamy order_value, ale TYLKO jeśli ten klucz istnieje!
    if 'order_value' not in missing_keys:
        if order['order_value'] <= 0:
            errors.append('Wartość zamówienia to 0 lub mniej')

    # Krok 3: Sprawdzamy status, TYLKO jeśli ten klucz istnieje!
    if 'status' not in missing_keys:
        if order['status'] not in allowed_statuses:
            errors.append('Niedozwolony status w słowniku')

for error in errors:
    print(error)

