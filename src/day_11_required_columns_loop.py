required_columns = ['order_id', 'customer_id', 'order_value', 'status']
columns_in_file = ['order_id', 'customer_id']
missing_columns = []

for required_column in required_columns:
    if required_column not in columns_in_file:
        missing_columns.append(required_column)

if len(missing_columns) == 0:
    print('Gratulacje, wszystkie kolumny są w pliku')
else:
    for missing_column in missing_columns:
        print(f'Brakująca kolumna: {missing_column}')


