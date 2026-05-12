file_metadata = {
    'file_name': 'raport_sprzedazy_2026.csv',
    'rows_count': 5430,
    'source_system': 'CRM_System',
    'error_percent': 1.5
}

errors = []

if file_metadata.get('file_name') is None:
    errors.append('W pliku brakuje klucza file_name')

if file_metadata.get('rows_count') is None:
    errors.append('W pliku brakuje klucza rows_count')
elif file_metadata['rows_count'] <= 0:
    errors.append('W pliku rows_count jest równy bądź mniejszy od zera')

if file_metadata.get('source_system') is None:
    errors.append('W pliku brakuje klucza source_system')

if file_metadata.get('error_percent') is None:
    errors.append('W pliku brakuje klucza error_percent')
elif file_metadata['error_percent'] >= 5:
    errors.append('Procent błędów w pliku jest większy bądź równy 5')

if not errors:
    print('Plik ma się dobrze')
else:
    for error in errors:
        print(error)