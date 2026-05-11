order = {
    'order_id': 123,
    'order_value': 399,
    'status': 'lwaa'
}

allowed_statuses = ['paid', 'cancel', 'pending']
errors = []

if order['order_value'] <= 0:
    errors.append('Wartość zamówienia jest mniejsza bądź równa 0.')

if order['status'] not in allowed_statuses:
    errors.append(f'Niedozwolony status w zamówieniu: {order['status']}')

if len(errors) == 0:
    print('Brak błędów')
else:
    for error in errors:
        print(error)