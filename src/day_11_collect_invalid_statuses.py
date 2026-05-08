statuses = ['pending', 'errors', 'processing', 'completed', 'failed', 'cancelled', 'on_hold', 'queued', 'in_progress', 'approved', 'rejected', 'retrying']
allowed_statuses = ['pending', 'processing', 'completed', 'failed']
errors = []
erros_count = 0

for status in statuses:
    if status not in allowed_statuses:
        errors.append(status)
        errors_count =+ 1

if errors_count == 0:
    print('Wszystkie statusy są poprawne')
else:
    for error in errors:
        print(f'Błędny status: {error}')
    print(f'Liczba błędów to: {len(errors)}')


