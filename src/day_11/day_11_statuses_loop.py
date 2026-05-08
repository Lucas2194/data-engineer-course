statuses = ['pending', 'errors', 'processing', 'completed', 'failed', 'cancelled', 'on_hold', 'queued', 'in_progress', 'approved', 'rejected', 'retrying']
allowed_staties = ['pending', 'processing', 'completed', 'failed']

for status in statuses:
    if status in allowed_staties:
        print(f'Status poprawny: {status}')
    else:
        print(f'Status niepoprawny: {status}')