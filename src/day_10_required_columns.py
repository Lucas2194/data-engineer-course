required_rows = ['order_id', 'customer_id', 'order_value', 'status']

user_row = input('Podaj nazwę kolumny: ')
user_row = user_row.lower()

if user_row in required_rows:
    print('Kolumna jest wymagana')
else:
    print('Kolumna nie jest wymagana')