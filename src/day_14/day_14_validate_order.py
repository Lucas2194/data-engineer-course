def validate_order(order):
    errors = []
    allowed_statuses = ['paid', 'cancel', 'pending']

    if order.get('order_id') is None:
        errors.append('Brakuje klucza identyfikacji zamówienia')
    
    if order.get('order_value') is None:
        errors.append('Brakuje klucza wartości zamówienia')
    elif order['order_value'] <= 0:
        errors.append('Wartość zamówienia jest mniejsza bądź równa 0')
    
    if order.get('status') is None:
        errors.append('Brakuje klucza status w zamówieniu')
    elif order['status'] not in allowed_statuses:
        errors.append('Niedozwolony status zamówienia')

    return errors

order_one = validate_order({
    'order_id': 1,
    'order_value': 199.99,
    'status': 'paid'
})   

order_two = validate_order({
    'order_id': 302,
    'order_value': 50.00
    # 2. Celowy błąd: brak klucza 'status'
})

print(order_one)
print(order_two)