order = {
    'order_id': 123,
    'order_value': 199
}

if order.get('status') is None:
    print('Brakuje klucza status')

print(order.get('status', 'unknown'))