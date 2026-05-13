def get_orders():
    return [
        {
            'order_id': 2001,
            'order_value': 149.99,
            'status': 'paid'
        },  # 1. Poprawne
        {
            # 2. Błąd: brak order_id
            'order_value': 25.50,
            'status': 'new'
        },
        {
            'order_id': 2003,
            # 3. Błąd: brak order_value
            'status': 'shipped'
        },
        {
            'order_id': 2004,
            'order_value': -15.00,   # 4. Błąd: order_value < 0
            'status': 'paid'
        },
        {
            'order_id': 2005,
            'order_value': 300.00
            # 5. Błąd: brak statusu
        },
        {
            'order_id': 2006,
            'order_value': 89.99,
            'status': 'zablokowane'  # 6. Błąd: niedozwolony status
        },
        {
            'order_id': 2007,
            'order_value': 0,        # 7. Błąd: order_value == 0
            'status': 'new'
        },
        {
            'order_id': 2008,
            'order_value': 999.00,
            'status': 'shipped'
        }   # 8. Poprawne
    ]

def is_valid_status(status):
    allowed_statuses = ['shipped', 'new', 'paid']
    return status in allowed_statuses

def validate_order(order):
    
    errors = []

    if order.get('order_id') is None:
        errors.append(f'Zamówienie ID: {order.get("order_id", "BRAK")} - Brakuje klucza identyfikacji zamówienia')
    
    if order.get('order_value') is None:
        errors.append(f'Zamówienie ID: {order.get("order_id", "BRAK")} - Brakuje klucza wartości zamówienia')
    elif order['order_value'] <= 0:
        errors.append(f'Zamówienie ID: {order.get("order_id", "BRAK")} - Wartość zamówienia jest mniejsza bądź równa 0')
    
    if order.get('status') is None:
        errors.append(f'Zamówienie ID: {order.get("order_id", "BRAK")} - Brakuje klucza status w zamówieniu')
    elif not is_valid_status(order['status']):
        errors.append(f'Zamówienie ID: {order.get("order_id", "BRAK")} - Niedozwolony status zamówienia')

    return errors

def validate_orders(orders):  
    
    errors = []

    for order in orders:
        errors.extend(validate_order(order))
    return errors

def print_validation_report(errors):
    print('--- RAPORT WALIDACJI ---')
    if not errors:
        print('Wszystkie zamówienia są poprawne')
    else:
        for error in errors:
            print(error)

orders = get_orders()
errors = validate_orders(orders)
print_validation_report(errors)