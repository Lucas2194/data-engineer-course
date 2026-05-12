orders = [
    {
        'order_id': 301,
        'order_value': 199.99,
        'status': 'sent'
    },  # 1. Zamówienie w pełni poprawne
    {
        'order_id': 302,
        'order_value': 50.00
        # 2. Celowy błąd: brak klucza 'status'
    },
    {
        'order_id': 303,
        'order_value': 120.50,
        'status': 'unknown' # 3. Celowy błąd: status 'unknown'
    },
    {
        'order_id': 304,
        'order_value': 0,   # 4. Celowy błąd: order_value <= 0
        'status': 'pending'
    },
    {
        'order_id': 305,
        # 5. Celowy błąd: brak klucza 'order_value'
        'status': 'cancel'
    }
]

errors = []
rekord = 1 
allowed_statuses = ['sent', 'pending', 'cancel']


for order in orders:
    if order.get('order_id') is None:
        errors.append(f'W rekordzie {rekord} brakuje numeru zamówienia')
    if order.get('order_value') is None:
        errors.append(f'W rekordzie {rekord} brakuje klucza wartości zamówienia')
    elif order['order_value'] <= 0:
        errors.append(f'W rekordzie {rekord} wartość zamówienia jest mniejsza bądź równa 0')
    if order.get('status') is None:
        errors.append(f'W rekodzie {rekord} brakuje klucza status')
    elif order['status'] not in allowed_statuses:
        errors.append(f'W rekordzie {rekord} jest nieddozowlony status zamówienia')
    rekord = rekord + 1

if not errors:
    print('Zamówienie poprawne')
else:
    for error in errors:
        print(error)