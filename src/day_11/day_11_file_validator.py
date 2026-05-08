file_name = 'dane_sprzedazowe.csv'
rows_count = 5430
available_columns = ['order_id', 'customer_id', 'status']
required_columns = ['order_id', 'customer_id', 'order_value', 'status']
allowed_statuses = ['pending', 'completed', 'cancelled', 'errors']
statuses_in_file = ['completed', 'pending', 'unknown_status', 'completed']

errors = []

if file_name == '':
    errors.append('Plik nie ma nazwy')

if rows_count <= 0:
    errors.append('Plik ma liczbą wierszy mniejszą lub równą 0')

for required_column in required_columns:
    if required_column not in available_columns:
        errors.append(f'Kolumna {required_column} która jest wymagana, nie znajduję się w pliku')

for status_in_file in statuses_in_file:
    if status_in_file not in allowed_statuses:
        errors.append(f'Status {status_in_file} nie jest dozwolony w pliku')

print('Podsumowanie')
print('---------------')

for error in errors:
    print(error)