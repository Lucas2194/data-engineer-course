orders = [
    {
        'order_id': 1001,
        'order_value': 250.00,
        'status': 'paid'
    },  # 1. Poprawne
    {
        # 2. Błąd: brak order_id
        'order_value': 45.50,
        'status': 'new'
    },
    {
        'order_id': 1003,
        # 3. Błąd: brak order_value
        'status': 'shipped'
    },
    {
        'order_id': 1004,
        'order_value': 0,   # 4. Błąd: order_value <= 0
        'status': 'paid'
    },
    {
        'order_id': 1005,
        'order_value': 120.00
        # 5. Błąd: brak statusu
    },
    {
        'order_id': 1006,
        'order_value': 89.99,
        'status': 'invalid_status' # 6. Błąd: niedozwolony status
    },
    {
        'order_id': 1007,
        'order_value': 500.00,
        'status': 'new'
    }   # 7. Poprawne (dla lepszych statystyk w raporcie)
]

allowed_statuses = ['new', 'paid', 'shipped'] 

errors = []

record = 1
correct_record = 0
incorrect_records = 0

for order in orders:
    record_errors = []

    if order.get('order_id') is None:
        record_errors.append(f'W rekordzie {record} brakuje numeru zamówienia')
    
    if order.get('order_value') is None:
        record_errors.append(f'W rekordzie {record} brakuje wartości zamówienia')
    elif order['order_value'] < 0:
        record_errors.append(f'W rekordzie {record} wartość zamówienia jest mniejsza od 0')
    
    if order.get('status') is None:
        record_errors.append(f'W rekodzie {record} brakuje klucza status')
    elif order['status'] not in allowed_statuses:
        record_errors.append(f'W rekordzie {record} jest nieprawidłowy status: {order['status']}')
    
    if not record_errors:
        correct_record = correct_record + 1
    else:
        errors.extend(record_errors)
        incorrect_records = incorrect_records + 1
    
    record = record + 1 

print('Raport')
print('------------')

print(f'Liczba wszystkich rekordów to: {record - 1}')
print(f'Liczba poprawnych rekordów to: {correct_record}')
print(f'Liczba błędnych rekordów to: {incorrect_records}')
print('Lista Błędów: ')

if not errors:
    print('Brak błędów w plikach')
else:
    for error in errors:
        print(error)
