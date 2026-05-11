order = {
    'order_id': 1001,
    'price': 125,
    'category': 'animals',
    'status': 'paid'
}

required_keys = ['order_id', 'order_value', 'status']

missing_keys = []

for required_key in required_keys:
    print(order)
    if required_key not in order:
        missing_keys.append(required_key)

if len(missing_keys) == 0:
    print('Rekord ma wszystkie wymaganane pola')
else:
    for missing_key in missing_keys:
        print(f'Brakuje klucza: {missing_key}')