order = {
    "order_id": 1002,
    "order_value": 349.99,
    "status": 'pending'
}

allowed_statuses = ['sent', 'pending', 'cancel']

errors = []

if order.get('order_id') is None:
    errors.append('W zamówieniu brakuje klucza order_id')

if order.get('order_value') is None:
    errors.append('W zamówieniu brakuje klucza order_value')
else:
    if order['order_value'] <= 0:
        errors.append('W zamówieniu wartość jego jest mniejsza bądź równa 0')

if order.get('status') is None:
    errors.append('W zamówieniu brakuje statusu')
else:
    if order['status'] not in allowed_statuses:
        errors.append('Niedozwolony status w zamówieniu')

if not errors:
    print('Zamówienie poprawne')
else:
    for error in errors:
        print(error)

