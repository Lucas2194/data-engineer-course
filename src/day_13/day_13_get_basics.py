order = {
    'order_id': 123,
    'order_value': 199
}

print(order.get('status'))
print(order.get('status', 'unknown'))

if order.get('status') is None:
    print('Brakuje statusu')

